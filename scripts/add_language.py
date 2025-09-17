import uuid
import yaml
from _github_utilities import (
    create_branch,
    get_file_in_repository,
    write_file,
    send_pull_request,
)

def add_language_to_resources_yml(repository, file_path="resources/nfdi4bioimage.yml", parent_branch="main"):
    """
    Add language to entries under the 'resources' section in a YAML file if missing.

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
    from transformers import pipeline

    model_ckpt = "papluca/xlm-roberta-base-language-detection"
    pipe = pipeline("text-classification", model=model_ckpt)

    def detect_language(text):
        print("determining language for", text)
        lang = pipe([text], top_k=1, truncation=True)[0][0]["label"]
        print("language is", lang)
        return lang 


    # Load YAML file content
    content_file = get_file_in_repository(repository, parent_branch, file_path)
    content = yaml.safe_load(content_file.decoded_content)

    # Add language to resources without one
    modified = False
    for resource in content.get("resources", []):
        if "description" in resource and len(resource["description"]) > 200: # without detailed description, we can't determine the language
            if "language" not in resource or len(resource["language"]) == 0:
                text = ""
                if "name" in resource:
                    text += resource["name"]
                if "description" in resource:
                    text += resource["description"]
                resource["language"] = detect_language(text)
                if len(resource["language"]) > 0:
                    modified = True

    # Write updated YAML content back to the branch
    if modified:
        # Create a new branch
        branch_name = create_branch(repository, parent_branch=parent_branch)
        updated_content = yaml.dump(content, sort_keys=False, allow_unicode=True)
        write_file(repository, branch_name, file_path, updated_content, commit_message="Add missing language to resources")

        # Send a pull request
        pr_title = "Add missing language to resources"
        pr_description = f"Adds missing language to resources in the {file_path}. "
        pr_url = send_pull_request(repository, branch_name, pr_title, pr_description)
        print(pr_url)
    else:
        print("No modifications made to the resources file")

if __name__ == "__main__":
    import sys
    repository = sys.argv[1]
    add_language_to_resources_yml(repository)
