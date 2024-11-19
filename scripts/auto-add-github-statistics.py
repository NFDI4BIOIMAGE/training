import os
import pandas as pd
from datetime import datetime

def extract_github_repos(yaml_data):
    """Extract GitHub repository URLs from the YAML data.
    
    Parameters
    ----------
    yaml_data : dict
        Data loaded from the YAML file.
    
    Returns
    -------
    list of str
        List of GitHub repository URLs.
    """
    repos = []
    for resource in yaml_data.get('resources', []):
        urls = resource.get('url', [])
        if isinstance(urls, str):
            urls = [urls]
        for url in urls:
            if url.startswith("https://github.com/"):
                url = url.replace("https://github.com/", "")
                if url.endswith("/"):
                    url = url[:-1]
                if len(url.split("/")) > 2:
                    url = "/".join(url.split("/")[:2])
                repos.append(url)
    return repos

def get_repo_stats(repo_name):
    """Retrieve the number of stars and forks for a given GitHub repository.
    
    Parameters
    ----------
    repo_name : str
        Name of the repository in 'user/repo' format.
    
    Returns
    -------
    dict
        Dictionary containing stars and forks count.
    """
    print(f"-> get_repo_stats({repo_name})")
    from _github_utilities import get_github_repository

    repo = get_github_repository(repo_name)
    return {
        "repo_name": repo_name,
        "stars": repo.stargazers_count,
        "forks": repo.forks_count
    }

def main():

    from generate_link_lists import all_content
    from _github_utilities import create_branch, get_file_in_repository, get_issue_body, write_file, send_pull_request

    yaml_data = all_content('./resources/')
    repos = extract_github_repos(yaml_data)

    stats_list = [get_repo_stats(repo) for repo in repos]
    df = pd.DataFrame(stats_list)

    today = datetime.now().strftime('%Y%m%d')
    output_dir = 'github_statistics'
    os.makedirs(output_dir, exist_ok=True)
    output_file = f"{output_dir}/{today}.csv"
    df.to_csv(output_file, index=False)


    # upload to github and send a pull-request
    repository = "nfdi4bioimage/training"
    branch = create_branch(repository)
    with open(output_file, 'r') as file:
        file_content = file.read()

    write_file(repository, branch, output_file, file_content, "Add " + output_file)
    res = send_pull_request(repository, branch, f"Add {output_file}", "")

if __name__ == "__main__":
    main()
