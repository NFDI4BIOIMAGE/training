import os
import streamlit as st
from github import Github
import yaml

# GitHub authentication
GITHUB_API_KEY = os.getenv('GITHUB_API_KEY')  # Get the API key from environment variable
if not GITHUB_API_KEY:
    st.error("GitHub API Key is not set in the environment variables.")
    st.stop()

try:
    g = Github(GITHUB_API_KEY)
    repo = g.get_repo("SeverusYixin/Test_Appsubmitter")  # My GitHub Repositories for test Appsubmitter
except Exception as e:
    st.error(f"Failed to authenticate with GitHub: {e}")
    st.stop()

st.title("GitHub Training Materials Submission")

st.markdown("""
Welcome to the GitHub Training Materials Submission app!

Use this form to add new training materials to our GitHub repository. 
Please fill in the details below and click "Submit".

Steps:
1. Select the YAML file for the type of training material.
2. Provide the necessary information.
3. Submit the form to create an issue and a pull request.

Thank you for your contribution!
""")

# Form to collect user input
with st.form(key='submission_form'):
    submitter_name = st.text_input("Submitter Name")
    authors = st.text_input("Authors")
    license = st.text_input("License")
    name = st.text_input("Name")
    description = st.text_area("Description")
    tags = st.text_input("Tags (comma-separated)")
    type_ = st.text_input("Type (comma-separated)")
    url = st.text_input("URL")
    yaml_file = st.selectbox("YAML File", [
        'blog_posts.yml', 'events.yml', 'materials.yml', 'nfdi4bioimage.yml', 'papers.yml', 'workflow-tools.yml', 'youtube_channels.yml'
    ])
    submit_button = st.form_submit_button(label='Submit')

# Handle form submission
if submit_button:
    # Create GitHub issue
    issue_title = f"Issue submitted by {submitter_name}"
    issue_body = (
        f"- authors: {authors}\n"
        f"  license: {license}\n"
        f"  name: {name}\n"
        f"  description: {description}\n"
        f"  tags:\n"
        + ''.join([f"    - {tag.strip()}\n" for tag in tags.split(',')]) +
        f"  type:\n"
        + ''.join([f"    - {type_.strip()}\n" for type_ in type_.split(',')]) +
        f"  url: {url}\n"
    )
    # Print the issue body to debug
    print("Generated issue body:\n", issue_body)
    
    try:
        issue = repo.create_issue(title=issue_title, body=issue_body)
        st.success(f"Issue created: {issue.html_url}")
    except Exception as e:
        st.error(f"Failed to create issue: {e}")

    # Edit YAML file
    try:
        # Include the 'resources' directory in the file path
        file_path = f"resources/{yaml_file}"
        file_contents = repo.get_contents(file_path)
        yaml_content = file_contents.decoded_content.decode('utf-8')
        
        # Display the original YAML content for debugging purposes
        st.text_area("Original YAML content", yaml_content)

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
            'tags': [tag.strip() for tag in tags.split(',')],
            'type': [type_.strip() for type_ in type_.split(',')],
            'url': url
        }

        resources_list.append(new_entry)
        yaml_data['resources'] = resources_list
        new_yaml_content = yaml.safe_dump(yaml_data, allow_unicode=True, sort_keys=False)

        # Create a new branch
        base_branch = repo.get_branch("main")
        new_branch_name = f"update-{yaml_file}-{submitter_name}".replace(' ', '-')
        repo.create_git_ref(ref=f"refs/heads/{new_branch_name}", sha=base_branch.commit.sha)

        # Commit changes to the new branch
        repo.update_file(file_path, f"Add new entry by {submitter_name}", new_yaml_content, file_contents.sha, branch=new_branch_name)

        # Create pull request with custom title and description
        pr_title = f"Add new training materials request to {yaml_file}"
        # pr_body = f"Added new training materials to {yaml_file} by {submitter_name}. Closes #{issue.number}"
        pr_body = f"Added new training materials to {yaml_file} by {submitter_name}.\n\nThis PR closes #{issue.number}"
        pr = repo.create_pull(title=pr_title, body=pr_body, head=new_branch_name, base='main')
        st.success(f"Pull request created: {pr.html_url}")
    except Exception as e:
        st.error(f"Failed to update YAML file and create pull request: {e}")

# cd ..\scripts
# streamlit run appsubmitter.py
