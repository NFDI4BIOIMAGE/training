import os
import yaml
import time
from github import Github
import streamlit as st
from pathlib import Path
import pandas as pd

def load_yaml_data(file_path):
    """
    Load YAML data from a file and modify it based on certain conditions.

    Args:
        file_path (str): Path to the YAML file.

    Returns:
        dict: Parsed and possibly modified YAML data.
    """
    with open(file_path, 'r', encoding="utf8") as file:
        data = yaml.safe_load(file)
        
        # Check for 'url' in data and append 'zenodo' to tags if the condition is met
        if "url" in data and "zenodo" in str(data["url"]).lower():
            if 'tags' in data and isinstance(data['tags'], list):
                data["tags"].append("zenodo")
            else:
                data['tags'] = ["zenodo"]
        
        return data
    

def all_content(directory_path):
    """
    Load all YAML data from a directory into a list of dictionaries.

    Args:
        directory_path (str): Path to the directory containing YAML files.

    Returns:
        list: List of all resources dictionaries from all YAML files.
    """
    resources = []
    for yaml_file in Path(directory_path).glob('*.yml'):
        yaml_data = load_yaml_data(yaml_file)
        if 'resources' in yaml_data:
            resources.extend(yaml_data['resources'])
    return {'resources': resources}

def get_unique_values_from_yamls(resources_dir):
    """
    Get unique tags, types, and licenses from YAML files using pandas for data processing.

    Args:
        resources_dir (str): Directory containing YAML files.

    Returns:
        tuple: Sorted lists of unique tags, types, and licenses.
    """
    content = all_content(resources_dir)
    df = pd.DataFrame(content['resources'])

    # Handle cases where 'tags', 'type', and 'license' might not be present or not lists
    df['tags'] = df['tags'].apply(lambda x: x if isinstance(x, list) else [])
    df['type'] = df['type'].apply(lambda x: [x] if isinstance(x, str) else x if isinstance(x, list) else ['Unknown'])
    df['license'] = df['license'].apply(lambda x: [x] if isinstance(x, str) else x if isinstance(x, list) else ['Unknown'])

    # Extract unique values
    unique_tags = sorted(set(tag for sublist in df['tags'] for tag in sublist))
    unique_types = sorted(set(t for sublist in df['type'] for t in sublist))
    unique_licenses = sorted(set(l for sublist in df['license'] for l in sublist))

    return unique_tags, unique_types, unique_licenses


def get_yaml_files(resources_dir):
    """
    List YAML files in a directory.

    Args:
        resources_dir (str): Directory containing YAML files.

    Returns:
        list: Sorted list of YAML file names.
    """
    return sorted([str(yaml_file.name) for yaml_file in Path(resources_dir).glob('*.yml')])


def get_github_repository(repository):
    """
    Get the GitHub repository object.

    Args:
        repository (str): The full name of the GitHub repository (e.g., "username/repo-name").

    Returns:
        github.Repository.Repository: The GitHub repository object.
    """
    
    access_token = os.getenv('GITHUB_API_KEY')
    
    if not access_token:
        raise Exception("GitHub API Key is not set in the environment variables.")

    # Create a PyGithub instance using the access token
    g = Github(access_token)

    # Get and return the repository object
    return g.get_repo(repository)

def create_pull_request(repo, yaml_file, authors, license, name, description, tags, type_, url):
    """
    Create a pull request to add a new entry to a YAML file on GitHub.

    Args:
        repo (Repository): Repository object.
        yaml_file (str): YAML file to update.
        authors (str): Authors of the new entry.
        license (str): License of the new entry.
        name (str): Name of the new entry.
        description (str): Description of the new entry.
        tags (list): Tags for the new entry.
        type_ (str): Type of the new entry.
        url (str): URL of the new entry.

    Raises:
        Exception: If the pull request creation fails.
    """
    try:
        file_path = f"resources/{yaml_file}"
        file_contents = repo.get_contents(file_path)
        yaml_content = file_contents.decoded_content.decode('utf-8')
        yaml_data = yaml.safe_load(yaml_content)
        new_entry = {
            'authors': authors,
            'license': license,
            'name': name,
            'description': description,
            'tags': tags,
            'type': type_,
            'url': url
        }
        if 'resources' in yaml_data:
            yaml_data['resources'].append(new_entry)
        else:
            yaml_data['resources'] = [new_entry]
        new_yaml_content = yaml.safe_dump(yaml_data, allow_unicode=True, sort_keys=False)
        base_branch = repo.get_branch("main")
        timestamp = int(time.time())
        branch_name = f"update-{yaml_file.split('.')[0]}-{timestamp}".replace(' ', '-')
        repo.create_git_ref(ref=f"refs/heads/{branch_name}", sha=base_branch.commit.sha)
        repo.update_file(file_path, f"Add new entry", new_yaml_content, file_contents.sha, branch=branch_name)
        pr_title = f"Add new training materials request to {yaml_file}"
        pr_body = "Added new training materials."
        pr = repo.create_pull(title=pr_title, body=pr_body, head=branch_name, base='main')
        st.success(f"Pull request created: {pr.html_url}")
    except Exception as e:
        st.error(f"Failed to update YAML file and create pull request: {e}")


# Path to resources directory
resources_dir = Path('..') / 'resources'

# Extract dynamic values from YAML files
unique_tags, unique_types, unique_licenses = get_unique_values_from_yamls(resources_dir)

# Get list of YAML files dynamically
yaml_files = get_yaml_files(resources_dir)

# Directly get the GitHub repository object
repo = get_github_repository("NFDI4BIOIMAGE/training")

st.title("GitHub Training Materials Submission")
st.markdown("Welcome to the GitHub Training Materials Submission app! Please fill in the details below and click 'Submit'. Thank you for your contribution!")

with st.form(key='submission_form'):
    authors = st.text_input("Authors")
    license = st.multiselect("Licenses", unique_licenses)
    name = st.text_input("Name")
    description = st.text_area("Description")
    
    tags = st.multiselect("Tags", unique_tags)
    
    tags_input = st.text_input("Add tags which are not in the select list (comma separated)", "")

    type_ = st.multiselect("Types", unique_types)
    url = st.text_input("URL")
    
    yaml_file = st.selectbox("YAML File", ["Select a YAML file"] + yaml_files)
    
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    if tags_input:
        entered_tags = [tag.strip() for tag in tags_input.split(',') if tag.strip()]
        tags.extend(entered_tags)
    
    tags = sorted(set(tags))
    
    if not license or yaml_file == "Select a YAML file":
        st.error("Please make sure all selections are made.")
    else:
        create_pull_request(repo, yaml_file, authors, license, name, description, tags, type_, url)
