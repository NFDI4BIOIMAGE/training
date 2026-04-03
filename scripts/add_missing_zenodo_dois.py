import requests
import yaml
from _github_utilities import create_branch, write_file, send_pull_request, get_github_repository

def fetch_doi_from_zenodo(zenodo_url):
    """
    Fetches DOI information from the Zenodo URL using the Zenodo REST API.

    Parameters
    ----------
    zenodo_url : str
        A Zenodo record URL (e.g., https://zenodo.org/record/4071471).

    Returns
    -------
    str or None
        The corresponding DOI URL (e.g., https://doi.org/10.xxxx), or None if not found.
    """
    record_id = zenodo_url.split("/")[-1]
    api_url = f"https://zenodo.org/api/records/{record_id}"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        return f"https://doi.org/{data['doi']}"
    return None

def add_missing_dois(repository, file_path):
    """
    Adds missing DOI links to the resources YAML file and commits changes.

    Parameters
    ----------
    repository : str
        The full name of the GitHub repository (e.g., "username/repo-name").
    file_path : str
        Path to the YAML file (e.g., resources/nfdi4bioimage.yml).
    """
    # Authenticate and fetch file content
    repo = get_github_repository(repository)
    main_branch = "main"
    file_content = repo.get_contents(file_path, ref=main_branch)
    content = yaml.safe_load(file_content.decoded_content.decode())

    # Modify content by adding missing DOIs
    modified = False
    for entry in content['resources']:
        urls = entry.get('url', [])
        if not isinstance(urls, list):
            urls = [urls]
        zenodo_links = [url for url in urls if "zenodo.org" in url]
        doi_links = [url for url in urls if "doi.org" in url]
        this_record_modified = False
        for zenodo_link in zenodo_links:
            if not doi_links:
                doi_url = fetch_doi_from_zenodo(zenodo_link)
                if doi_url:
                    urls.append(doi_url)
                    modified = True
                    this_record_modified = True
        if this_record_modified:
            entry['url'] = urls

    # Save changes and create a pull request if modified
    if modified:
        new_branch = create_branch(repository, parent_branch=main_branch)
        new_content = yaml.dump(content, sort_keys=False, allow_unicode=True)
        write_file(repository, new_branch, file_path, new_content, "Add missing DOIs to resources")
        pr_url = send_pull_request(
            repository,
            new_branch,
            "Add missing DOIs for Zenodo records",
            f"closes #{899}\n\nThis PR adds missing DOI links to the resources YAML file."
        )
        print(pr_url)

if __name__ == "__main__":
    import sys
    repository = sys.argv[1]
    add_missing_dois(repository, "resources/nfdi4bioimage.yml")
