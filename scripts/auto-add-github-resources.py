import sys
import os
from _github_utilities import create_branch, get_file_in_repository, get_issue_body, write_file, send_pull_request
import yaml
from github import Github, GithubException  

def main():
    """
    Main function to retrieve metadata from a GitHub repository and append it to a YAML file. 
    Creates a pull request with the updated data.

    Arguments:
    - repository (str): GitHub repository name.
    - issue (int): Issue number containing the GitHub link.

    Example(local_test):
    python scripts/auto-add-github-resources.py "nfdi4bioimage/training" 236
    """
    # Retrieve repository and issue number from command-line arguments
    repository = sys.argv[1]
    issue = int(sys.argv[2])

    yml_filename = "resources/nfdi4bioimage.yml"
    
    # Get the issue body, which should contain a GitHub repository link
    issue_text = get_issue_body(repository, issue)
    if "\n" in issue_text or not issue_text.startswith("https://github.com/"):
        print(issue_text, " is not a GitHub repository link. Exiting.")
        return

    github_repo_url = issue_text

    # Retrieve GitHub metadata
    github_data_dict = complete_github_data(github_repo_url)
    github_yml = "\n- " + yaml.dump(github_data_dict).replace("\n", "\n  ")

    # Read the existing YAML "database"
    branch = create_branch(repository)
    file_content = get_file_in_repository(repository, branch, yml_filename).decoded_content.decode()

    print("YAML file content length:", len(file_content))

    # Add the new entry
    file_content += github_yml

    # Save the updated content back to GitHub and create a pull request
    write_file(repository, branch, yml_filename, file_content, "Add " + github_repo_url)
    res = send_pull_request(repository, branch, "Add " + github_repo_url, f"closes #{issue}")

    print("Done.", res)

def complete_github_data(github_repo_url):
    """
    Retrieves metadata from the specified GitHub repository with checks for missing fields.

    Arguments:
    - github_repo_url (str): The URL of the GitHub repository to retrieve metadata from.

    Returns:
    - entry (dict): A dictionary containing the repository metadata in the correct order.
    """
    token = os.getenv("GITHUB_API_KEY")
    if not token:
        raise Exception("GitHub API key not found. Please set GITHUB_API_KEY.")

    g = Github(token)
    repo_path = github_repo_url.replace("https://github.com/", "")
    repo = g.get_repo(repo_path)

    entry = {}

    # Contributors (Full name if available, otherwise username)
    try:
        contributors = repo.get_contributors()
        if contributors.totalCount > 0:
            # Use the contributor's full name if available, otherwise use the username
            entry['author'] = ", ".join([contrib.name if contrib.name else contrib.login for contrib in contributors])
        else:
            entry['author'] = ""
    except GithubException as e:
        if e.status == 403:
            print(f"403 error: Cannot access contributors for {repo.full_name}. Skipping this step.")
            entry['author'] = "Contributors not accessible"
        else:
            raise e

    # Repository description
    entry['description'] = repo.description if repo.description else ""

    # License information (stored as "license")
    try:
        license_info = repo.get_license()
        if license_info is not None:
            entry['license'] = license_info.license.name
    except:
        pass

    # Repository name
    entry['name'] = repo.name

    # Publication date (first release date or creation date)
    entry['publication_date'] = get_publication_date(repo)

    # Tags: always add the message "Dear users, please add tags."
    entry['tags'] = "TODO"

    # Type: Always set this field to "GitHub Repository"
    entry['type'] = "GitHub Repository"

    # Repository URL
    entry['url'] = github_repo_url

    return entry

def get_publication_date(repo):
    """
    Retrieves the publication date of the repository. If the repository has releases,
    the date of the first release is used. If no releases are found, the repository's
    creation date is used as the publication date.

    Arguments:
    - repo (github.Repository.Repository): The GitHub repository object.

    Returns:
    - publication_date (str): The ISO-formatted publication date.
    """
    releases = repo.get_releases()
    if releases.totalCount > 0:
        first_release = releases[0]
        return first_release.created_at.isoformat()
    elif repo.created_at is not None:
        return repo.created_at.isoformat()


if __name__ == "__main__":
    main()
