# This file contains utility functions using the github API via github-python:
# https://github.com/PyGithub/PyGithub (licensed LGPL3)
# Adapted from https://github.com/haesleinhuepf/git-bob/blob/main/src/git_bob/_github_utilities.py 
import os
from functools import lru_cache

@lru_cache(maxsize=1)
def get_github_repository(repository):
    """
    Get the GitHub repository object.

    Parameters
    ----------
    repository : str
        The full name of the GitHub repository (e.g., "username/repo-name").

    Returns
    -------
    github.Repository.Repository
        The GitHub repository object.
    """
    from github import Github
    access_token = os.getenv('GITHUB_API_KEY')

    # Create a PyGithub instance using the access token
    g = Github(access_token)

    # Get the repository object
    return g.get_repo(repository)

def get_issue_body(repository, issue):
    """
    Retrieve the body of a specific GitHub issue.

    Parameters
    ----------
    repository : str
        The full name of the GitHub repository (e.g., "username/repo-name").
    issue : int
        The issue number to retrieve the conversation for.

    Returns
    -------
    str
        The issue body.
    """
    print(f"-> get_conversation_on_issue({repository}, {issue})")

    repo = get_github_repository(repository)

    # Get the issue by number
    issue_obj = repo.get_issue(issue)

    # Get the body as a string
    return issue_obj.body

def write_file(repository, branch_name, file_path, new_content, commit_message="Update file"):
    """
    Modifies or creates a specified file with new content and saves the changes in a new git branch.
    The name of the new branch is returned.

    Parameters
    ----------
    repository : str
        The full name of the GitHub repository (e.g., "username/repo-name").
    branch_name : str
        The name of the branch where the file will be modified or created.
    file_path : str
        A file path within the repository to change the contents of.
    new_content : str
        Text content that should be written into the file.
    commit_message : str, optional
        The commit message for the changes. Default is "Update file".

    Returns
    -------
    str
        The name of the branch where the changed file is stored.
    """
    print(f"-> write_file_in_new_branch({repository}, {branch_name}, {file_path}, ...)")

    # Authenticate with GitHub
    repo = get_github_repository(repository)

    # Commit the changes
    if check_if_file_exists(repository, branch_name, file_path):
        file = get_file_in_repository(repository, branch_name, file_path)
        print(file.path)
        print(file_path)
        repo.update_file(file.path, commit_message, new_content, file.sha, branch=branch_name)
    else:
        repo.create_file(file_path, commit_message, new_content, branch=branch_name)

    return f"File {file_path} successfully created in repository {repository} branch {branch_name}."


@lru_cache(maxsize=1)
def get_file_in_repository(repository, branch_name, file_path):
    """
    Helper function to prevent multiple calls to the GitHub API for the same file.

    Parameters
    ----------
    repository : str
        The full name of the GitHub repository (e.g., "username/repo-name").
    branch_name : str
        The name of the branch to get the file content from.
    file_path : str
        The path of the file in the repository.

    Returns
    -------
    github.ContentFile.ContentFile
        The content file object of the specified file.
    """
    print("loading file content...", file_path)
    repo = get_github_repository(repository)
    return repo.get_contents(file_path, ref=branch_name)
    

def create_branch(repository, parent_branch="main"):
    """
    Creates a new branch in a given repository, derived from an optionally specified parent_branch and returns the name of the new branch.

    Parameters
    ----------
    repository : str
        The full name of the GitHub repository (e.g., "username/repo-name").
    parent_branch : str, optional
        The name of the parent branch from which the new branch will be created. Default is "main".

    Returns
    -------
    str
        The name of the newly created branch.
    """
    print(f"-> create_branch({repository}, {parent_branch})")

    import random
    import string

    # Authenticate with GitHub
    repo = get_github_repository(repository)

    # Get the main branch
    main_branch = repo.get_branch(parent_branch)

    # Create a new branch
    new_branch_name = "git-bob-mod-" + ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    repo.create_git_ref(ref=f"refs/heads/{new_branch_name}", sha=main_branch.commit.sha)

    return new_branch_name


def check_if_file_exists(repository, branch_name, file_path):
    """
    Checks if a specified file_path exists in a GitHub repository. Returns True if the file exists, False otherwise.

    Parameters
    ----------
    repository : str
        The full name of the GitHub repository (e.g., "username/repo-name").
    branch_name: str
        The name of the branch to check the file in.
    file_path : str
        The path of the file to check.

    Returns
    -------
    bool
        True if the file exists, False otherwise.
    """
    print(f"-> check_if_file_exists({repository}, {file_path})")

    try:
        # Try to get the contents of the file
        get_file_in_repository(repository, branch_name, file_path)
        return True
    except:
        return False


def send_pull_request(repository, branch_name, title, description):
    """
    Create a pull request from a defined branch into the main branch.

    Parameters
    ----------
    repository : str
        The full name of the GitHub repository (e.g., "username/repo-name").
    branch_name : str
        The name of the branch that should be merged into main.
    title : str
        A one-liner explaining what was changed in the branch.
    description : str
        A more detailed description of what has happened.
        If the changes are related to an issue write "closes #99 "
        where 99 stands for the issue number the pull-request is related to.

    Returns
    -------
    str
        The URL to the pull-request that was just created.
    """
    print(f"-> send_pull_request({repository}, {branch_name}, ...)")

    # Authenticate with GitHub
    repo = get_github_repository(repository)

    # Create a pull request
    pr = repo.create_pull(title=title, body=description, head=branch_name, base="main")

    return f"Pull request created: {pr.html_url}"
