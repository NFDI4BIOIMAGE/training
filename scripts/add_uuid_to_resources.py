import uuid
import yaml
from scripts._github_utilities import (
    create_branch,
    get_file_in_repository,
    write_file,
    send_pull_request,
)

def add_uuids_to_resources_yml(repository, file_path="resources/nfdi4bioimage.yml", parent_branch="main", issue_number=None):
    """
    Add UUIDs to entries under the 'resources' section in a YAML file if missing.

    Parameters
    ----------
    repository : Repository
        The GitHub repository object.
    file_path : str, optional
        Path to the YAML file in the repository, by default "resources/nfdi4bioimage.yml".
    parent_branch : str, optional
        The branch to create a new branch from, by default "main".
    issue_number : int, optional
        The issue number for linking the pull request, by default None.
    """
    # Create a new branch
    branch_name = create_branch(repository, parent_branch=parent_branch)

    # Load YAML file content
    content_file = get_file_in_repository(repository, parent_branch, file_path)
    content = yaml.safe_load(content_file.decoded_content)

    # Add UUIDs to resources without one
    for resource in content.get("resources", []):
        if "uuid" not in resource:
            resource["uuid"] = str(uuid.uuid4())

    # Write updated YAML content back to the branch
    updated_content = yaml.dump(content, sort_keys=False)
    write_file(repository, branch_name, file_path, updated_content, commit_message="Add missing UUIDs to resources")

    # Send a pull request
    pr_title = "Add missing UUIDs to resources"
    pr_description = f"Adds missing UUIDs to resources in the {file_path}. Closes #{issue_number}" if issue_number else pr_title
    send_pull_request(repository, branch_name, pr_title, pr_description)
