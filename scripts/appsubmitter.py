import os
import streamlit as st
from github import Github
import yaml
import time

def authenticate_with_github():
    """
    Authenticates with GitHub using the provided API key.

    Returns:
        g (Github): An instance of the Github class.
        repo (Repository): The repository object for the specified GitHub repository.
    """
    GITHUB_API_KEY = os.getenv('GITHUB_API_KEY')  # Get the API key from environment variable
    if not GITHUB_API_KEY:
        st.error("GitHub API Key is not set in the environment variables.")
        st.stop()

    try:
        g = Github(GITHUB_API_KEY)
        repo = g.get_repo("NFDI4BIOIMAGE/training")  # GitHub Repositories for Appsubmitter
    except Exception as e:
        st.error(f"Failed to authenticate with GitHub: {e}")
        st.stop()

    return g, repo

def create_pull_request(g, repo, yaml_file, authors, license, name, description, tags, type_, url):
    """
    Creates a pull request to add new training materials to the specified YAML file.

    Args:
        g (Github): An instance of the Github class.
        repo (Repository): The repository object for the specified GitHub repository.
        yaml_file (str): The name of the YAML file to update.
        authors (str): The authors of the training materials.
        license (str): The license for the training materials.
        name (str): The name of the training materials.
        description (str): The description of the training materials.
        tags (list): The tags associated with the training materials.
        type_ (list): The type of the training materials.
        url (str): The URL of the training materials.

    Returns:
        pr (PullRequest): The created pull request object.
    """
    try:
        # Include the 'resources' directory in the file path
        file_path = f"resources/{yaml_file}"
        file_contents = repo.get_contents(file_path)
        yaml_content = file_contents.decoded_content.decode('utf-8')

        yaml_data = yaml.safe_load(yaml_content)

        # Check the structure of the YAML data
        if 'resources' in yaml_data and isinstance(yaml_data['resources'], list):
            resources_list = yaml_data['resources']
        else:
            st.error("Unexpected YAML structure: Expected a dictionary with a 'resources' key containing a list.")
            st.stop()

        new_entry = {
            'authors': authors,
            'license': license,
            'name': name,
            'description': description,
            'tags': tags,
            'type': type_,
            'url': url
        }

        resources_list.append(new_entry)
        yaml_data['resources'] = resources_list
        new_yaml_content = yaml.safe_dump(yaml_data, allow_unicode=True, sort_keys=False)

        # Create a new branch with a unique name based on the YAML file name and a timestamp
        base_branch = repo.get_branch("main")
        timestamp = int(time.time())
        branch_suffix = f"{yaml_file.split('.')[0]}-{timestamp}"
        new_branch_name = f"update-{branch_suffix}".replace(' ', '-')
        repo.create_git_ref(ref=f"refs/heads/{new_branch_name}", sha=base_branch.commit.sha)

        # Commit changes to the new branch
        repo.update_file(file_path, f"Add new entry", new_yaml_content, file_contents.sha, branch=new_branch_name)

        # Create pull request with custom title and description
        pr_title = f"Add new training materials request to {yaml_file}"
        pr_body = f"Added new training materials to {yaml_file}."
        pr = repo.create_pull(title=pr_title, body=pr_body, head=new_branch_name, base='main')
        st.success(f"Pull request created: {pr.html_url}")
    except Exception as e:
        st.error(f"Failed to update YAML file and create pull request: {e}")

# GitHub authentication
g, repo = authenticate_with_github()

st.title("GitHub Training Materials Submission")

st.markdown("""
Welcome to the GitHub Training Materials Submission app!

Use this form to add new training materials to our GitHub repository. 
Please fill in the details below and click "Submit".

Steps:
1. Select the YAML file for the type of training material.
2. Provide the necessary information.
3. Submit the form to create a pull request.

Thank you for your contribution!
""")

# List of licenses
licenses = sorted([
    "AGPL-3.0", "All-rights-reserved", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "BSD-License", "CC0",
    "CC0-1.0", "CC0-Licence (with some variations noted in dataset attributes)", "CC-BY-4.0", "CC-BY-NC-4.0",
    "CC-BY-NC-ND-3.0-DEED", "CC-BY-ND-SA-4.0", "CC-BY-SA-4.0", "GPL-2.0", "GPL-3.0", "MIT", "ODC-By-1.0",
    "Public-domain"
])
licenses.append("Unknown")

# List of tags
tags_list = sorted([
    "Arc", "Artificial Intelligence", "Big Data", "Bio-Image Analysis", "Bioimage Analysis", "Bioimage Data",
    "Bioinformatics", "Cellpose", "Cellprofiler", "Citing", "Clesperanto", "Conda", "Dask", "Data Analysis",
    "Data Protection", "Data Science", "Data Stewardship", "Dataplant", "Deep Learning", "Deployment", 
    "Diffusion Models", "Elastix", "Fair", "Fair-Principles", "Fiji", "Flim", "Git", "Github", "Gpu", 
    "Hackathon", "I3Dbio", "Image Data Management", "Image Registration", "Image Segmentation", "Imagej", 
    "Imagej Macro", "Itk", "Large Language Models", "Licensing", "Machine Learning", "Mamba", "Meta Data", 
    "Metadata", "Microscopy Image Analysis", "Napari", "Neubias", "Nfdi4Bioimage", "Notebook", "Notebooks", 
    "Omero", "Open Access", "Open Science", "Python", "Pytorch", "Quareo-Limi", "R", "Research Data Management", 
    "Science Communication", "Segmentation", "Sharing", "Teaching", "Tu Dresden", "Workflow", "Workflow Engine", 
    "Zarr", "Zenodo"
])
tags_list.append("Unknown")

# List of types
types_list = sorted([
    "Big Data", "Bioimage Analysis", "Blog", "Book", "Code", "Collection", "Conference Abstract", "Data", 
    "Dataset", "Document", "Documentation", "Event", "Forum Post", "Github Repository", "Jupyter Book", 
    "Notebook", "Online Course", "Online Tutorial", "Poster", "Practicals", "Preprint", "Presentation", 
    "Publication", "Publiction", "Python", "Slide", "Slides", "Tutorial", "Video", "Videos", "Workshop"
])
types_list.append("Unknown")

# List of YAML files
yaml_list = sorted([
    'blog_posts.yml', 'events.yml', 'materials.yml', 'nfdi4bioimage.yml', 'papers.yml', 'workflow-tools.yml', 'youtube_channels.yml'
])

# Form to collect user input
with st.form(key='submission_form'):
    authors = st.text_input("Authors")
    license = st.selectbox("License", ["Select a license"] + licenses, index=0)
    name = st.text_input("Name")
    description = st.text_area("Description")
    tags = st.multiselect("Tags", tags_list)
    type_ = st.multiselect("Type", types_list)
    url = st.text_input("URL")
    yaml_file = st.selectbox("YAML File", ["Select a YAML file"] + yaml_list, index=0)
    submit_button = st.form_submit_button(label='Submit')

# Handle form submission
if submit_button:
    if license == "Select a license":
        st.error("Please select a license.")
    elif yaml_file == "Select a YAML file":
        st.error("Please select a YAML file.")
    elif not tags:
        st.error("Please select at least one tag.")
    elif not type_:
        st.error("Please select at least one type.")
    else:
        create_pull_request(g, repo, yaml_file, authors, license, name, description, tags, type_, url)

