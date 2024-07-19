import os
import streamlit as st
from github import Github

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

st.title("GitHub Issue and Pull Request Creator")

st.markdown("""
Welcome to the GitHub Issue and Pull Request Creator app!

Use this form to submit new issues or pull requests to our GitHub repository.
Please provide the necessary details in the fields below and click "Submit".
""")

# Form to collect user input
with st.form(key='issue_form'):
    url = st.text_input("URL")
    author = st.text_input("Author")
    description = st.text_area("Description")
    license = st.text_input("License")
    tags = st.text_input("Tags (comma-separated)")
    types = st.text_input("Type(s) (comma-separated)")
    submit_button = st.form_submit_button(label='Submit')

# Handle form submission
if submit_button:
    # Create GitHub issue
    issue_title = f"Issue submitted by {author}"
    issue_body = (
        f"URL: {url}\n\n"
        f"Description: {description}\n\n"
        f"License: {license}\n\n"
        f"Tags: {tags}\n\n"
        f"Type(s): {types}"
    )
    try:
        issue = repo.create_issue(title=issue_title, body=issue_body)
        st.success(f"Issue created: {issue.html_url}")
    except Exception as e:
        st.error(f"Failed to create issue: {e}")

# cd ..\scripts
# streamlit run appsubmitter.py
