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
    types = st.text_input("Type(s) (comma-separated)")
    url = st.text_input("URL")
    yaml_file = st.selectbox("YAML File", ['blog_posts.yml', 'events.yml', 'materials.yml', 'nfdi4bioimage.yml', 'papers.yml', 'workflow-tools.yml', 'youtube_channels.yml'])
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
        + ''.join([f"    - {type_.strip()}\n" for type_ in types.split(',')]) +
        f"  url: {url}\n"
    )

    # Print the issue body to debug
    print("Generated issue body:\n", issue_body)

# issue_body = (
#     f"- authors: {authors}\n"
#     f"  license: {license}\n"
#     f"  name: {name}\n"
#     f"  description: {description}\n"
#     f"  tags:\n"
#     + ''.join([f"    - {tag.strip()}\n" for tag in tags.split(',')]) +
#     f"  type:\n"
#     + ''.join([f"    - {type_.strip()}\n" for type_ in types.split(',')]) +
#     f"  url: {url}\n"
# )





    try:
        issue = repo.create_issue(title=issue_title, body=issue_body)
        st.success(f"Issue created: {issue.html_url}")
    except Exception as e:
        st.error(f"Failed to create issue: {e}")

    # Edit YAML file
    try:
        file_contents = repo.get_contents(yaml_file)
        yaml_data = yaml.safe_load(file_contents.decoded_content)

        new_entry = {
            'authors': authors,
            'license': license,
            'name': name,
            'description': description,
            'tags': [tag.strip() for tag in tags.split(',')],
            'type': [type_.strip() for type_ in types.split(',')],
            'url': url
        }

        yaml_data.append(new_entry)
        new_yaml_content = yaml.safe_dump(yaml_data, allow_unicode=True, sort_keys=False)

        # Commit changes
        repo.update_file(file_contents.path, f"Add new entry by {submitter_name}", new_yaml_content, file_contents.sha)

        # Create pull request
        pr_title = f"New entry by {submitter_name}"
        pr_body = f"Added a new entry to {yaml_file} by {submitter_name}"
        pr = repo.create_pull(title=pr_title, body=pr_body, head='main', base='main')
        st.success(f"Pull request created: {pr.html_url}")
    except Exception as e:
        st.error(f"Failed to update YAML file and create pull request: {e}")

# cd ..\scripts
# streamlit run appsubmitter.py
