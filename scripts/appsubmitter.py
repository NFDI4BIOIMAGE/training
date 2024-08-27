import streamlit as st
import os
from github import Github
import yaml
import time
from pathlib import Path

def load_yaml_data(file_path):
    """
    Load YAML data from a file.

    Args:
        file_path (str): Path to the YAML file.

    Returns:
        dict: Parsed YAML data.
    """
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)
    

def get_unique_values_from_yamls(resources_dir):

    """
    Get unique tags, types, and licenses from YAML files.

    Args:
        resources_dir (str): Directory containing YAML files.

    Returns:
        tuple: Sorted lists of unique tags, types, and licenses.
    """
    unique_tags = set()
    unique_types = set()
    unique_licenses = set()

    for yaml_file in Path(resources_dir).glob('*.yml'):
        yaml_data = load_yaml_data(yaml_file)
        if 'resources' in yaml_data:
            for entry in yaml_data['resources']:
                # Handle 'tags'
                tags = entry.get('tags', [])
                if isinstance(tags, list):
                    unique_tags.update(tags)
                else:
                    unique_tags.add(tags)

                # Handle 'type'
                type_ = entry.get('type', 'Unknown')
                if isinstance(type_, list):
                    unique_types.update(type_)
                else:
                    unique_types.add(type_)

                # Handle 'license'
                license_ = entry.get('license', 'Unknown')
                if isinstance(license_, list):
                    unique_licenses.update(license_)
                else:
                    unique_licenses.add(license_)

    return sorted(unique_tags), sorted(unique_types), sorted(unique_licenses)


def get_yaml_files(resources_dir):
    """
    List YAML files in a directory.

    Args:
        resources_dir (str): Directory containing YAML files.

    Returns:
        list: Sorted list of YAML file names.
    """
    return sorted([str(yaml_file.name) for yaml_file in Path(resources_dir).glob('*.yml')])

def authenticate_with_github():
    """
    Authenticate with GitHub using the API key from environment variables.

    Returns:
        tuple: Authenticated GitHub instance and repository object.

    Raises:
        Exception: If authentication fails.
    """
    GITHUB_API_KEY = os.getenv('GITHUB_API_KEY')
    if not GITHUB_API_KEY:
        st.error("GitHub API Key is not set in the environment variables.")
        st.stop()

    try:
        g = Github(GITHUB_API_KEY)
        repo = g.get_repo("NFDI4BIOIMAGE/training")
    except Exception as e:
        st.error(f"Failed to authenticate with GitHub: {e}")
        st.stop()

    return g, repo

def create_pull_request(g, repo, yaml_file, authors, license, name, description, tags, type_, url):
    """
    Create a pull request to add a new entry to a YAML file on GitHub.

    Args:
        g (Github): Authenticated GitHub instance.
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

g, repo = authenticate_with_github()

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
        create_pull_request(g, repo, yaml_file, authors, license, name, description, tags, type_, url)
