import yaml
import os
import pandas as pd
from datetime import datetime
from github import Github

def load_yaml(file_path):
    """Load a YAML file from the specified file path.
    
    Parameters
    ----------
    file_path : str
        Path to the YAML file.
    
    Returns
    -------
    dict
        Parsed YAML data.
    """
    with open(file_path, 'r') as stream:
        return yaml.safe_load(stream)

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
                repos.append(url.replace("https://github.com/", ""))
    return repos

def get_repo_stats(g, repo_name):
    """Retrieve the number of stars and forks for a given GitHub repository.
    
    Parameters
    ----------
    g : Github
        Authenticated GitHub object.
    repo_name : str
        Name of the repository in 'user/repo' format.
    
    Returns
    -------
    dict
        Dictionary containing stars and forks count.
    """
    repo = g.get_repo(repo_name)
    return {
        "repo_name": repo_name,
        "stars": repo.stargazers_count,
        "forks": repo.forks_count
    }

def main():
    token = os.getenv("GITHUB_TOKEN")  # Use environment variable for security
    yaml_file = 'nfdi4bioimage.yml'
    if not token:
        raise ValueError("GitHub token must be set in the GITHUB_TOKEN environment variable.")

    g = Github(token)
    yaml_data = load_yaml(yaml_file)
    repos = extract_github_repos(yaml_data)

    stats_list = [get_repo_stats(g, repo) for repo in repos]
    df = pd.DataFrame(stats_list)

    today = datetime.now().strftime('%Y%m%d')
    output_dir = 'github_statistics'
    os.makedirs(output_dir, exist_ok=True)
    df.to_csv(f"{output_dir}/{today}.csv", index=False)

if __name__ == "__main__":
    main()
