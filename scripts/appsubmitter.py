import os
import yaml
import time
import streamlit as st

# Import the functions from other modules in the same folder
from generate_link_lists import load_dataframe
from _github_utilities import get_github_repository  

# directory path for resources
directory_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'resources')

def get_unique_values_from_yamls(resources_dir):
    """
    Get unique tags, types, and licenses from YAML files using pandas for data processing.

    Parameters
    ----------
    resources_dir : str
        Directory containing YAML files.

    Returns
    -------
    tuple
        Sorted lists of unique tags, types, and licenses.
    """
    # Use the imported load_dataframe function to get content in DataFrame format
    df = load_dataframe(resources_dir)

    # Handle cases where 'tags', 'type', and 'license' might not be present or not lists
    df['tags'] = df['tags'].apply(lambda x: x if isinstance(x, list) else [])
    df['type'] = df['type'].apply(lambda x: [x] if isinstance(x, str) else x if isinstance(x, list) else ['Unknown'])
    df['license'] = df['license'].apply(lambda x: [x] if isinstance(x, str) else x if isinstance(x, list) else [])

    # Extract unique values
    unique_tags = sorted(set(tag for sublist in df['tags'] for tag in sublist))
    unique_types = sorted(set(t for sublist in df['type'] for t in sublist))
    unique_licenses = sorted(set(l for sublist in df['license'] for l in sublist))

    return unique_tags, unique_types, unique_licenses

def create_pull_request(repo, yaml_file, authors, license, name, description, tags, type_, url):
    """
    Create a pull request to add a new entry to a YAML file on GitHub.

    Parameters
    ----------
    repo : Repository
        Repository object.
    yaml_file : str
        YAML file to update.
    authors : str
        Authors of the new entry.
    license : str
        License of the new entry.
    name : str
        Name of the new entry.
    description : str
        Description of the new entry.
    tags : list
        Tags for the new entry.
    type_ : str
        Type of the new entry.
    url : str
        URL of the new entry.

    Raises
    ------
    Exception
        If the pull request creation fails.
    """
    try:
        file_path = f"resources/{yaml_file}"
        file_contents = repo.get_contents(file_path)
        yaml_content = file_contents.decoded_content.decode('utf-8')

        new_entry = {
            'authors': authors,
            'license': license,
            'name': name,
            'description': description,
            'tags': tags,
            'type': type_,
            'url': url
        }

        # Use allow_unicode=True to ensure proper Unicode handling
        new_yaml_content = yaml_content + "\n- " + yaml.safe_dump(new_entry, allow_unicode=False, sort_keys=False).replace("\n", "\n  ")

        base_branch = repo.get_branch("main")
        timestamp = int(time.time())
        branch_name = f"update-{yaml_file.split('.')[0]}-{timestamp}".replace(' ', '-')

        # create branch
        repo.create_git_ref(ref=f"refs/heads/{branch_name}", sha=base_branch.commit.sha)

        # modify file on new branch
        repo.update_file(file_path, f"Add new entry", new_yaml_content, file_contents.sha, branch=branch_name)

        # submit pull request
        pr_title = f"Add new training materials request to {yaml_file}"
        pr_body = "Added new training materials."
        pr = repo.create_pull(title=pr_title, body=pr_body, head=branch_name, base='main')
        st.success(f"Pull request created: {pr.html_url}")
    except Exception as e:
        st.error(f"Failed to update YAML file and create pull request: {e}")

# Extract dynamic values from YAML files
unique_tags, unique_types, unique_licenses = get_unique_values_from_yamls(directory_path)

# Directly set the path to the single YAML file
yaml_file = 'nfdi4bioimage.yml'  

# Directly get the GitHub repository object
repo = get_github_repository("NFDI4BIOIMAGE/training")

st.title("Training Materials Submission")
st.markdown("Welcome to the Training Materials Submission app! Please fill in the details below and click 'Submit'. Thank you for your contribution!")

with st.form(key='submission_form'):
    name = st.text_input("Name")
    description = st.text_area("Description")

    authors = st.text_input("Authors")
    license = st.multiselect("Licenses", unique_licenses)

    tags = st.multiselect("Tags", unique_tags)
    
    tags_input = st.text_input("Add tags which are not in the select list (comma separated)", "")

    type_ = st.multiselect("Types", unique_types)
    url = st.text_input("URL")
    
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    if tags_input:
        entered_tags = [tag.strip() for tag in tags_input.split(',') if tag.strip()]
        tags.extend(entered_tags)
    
    tags = sorted(set(tags))
    
    if not license:
        st.error("Please make sure all selections are made.")
    else:
        create_pull_request(repo, yaml_file, authors, license, name, description, tags, type_, url)
