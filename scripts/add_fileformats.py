import yaml
from _github_utilities import get_github_repository, create_branch, write_file, send_pull_request
import requests

import requests
import re
import time

# Function to extract record ID from a Zenodo link
def extract_zenodo_record_id(url):
    if url.startswith("https://zenodo.org/record") or url.startswith("https://zenodo.org/doi"):
        return url.split("/")[-1].split(".")[-1]

    return None

# Function to fetch file formats from Zenodo using the record ID
def fetch_file_formats(record_id):
    if not record_id:
        return None
    api_url = f"https://zenodo.org/api/records/{record_id}"
    try:
        time.sleep(1)  # Add a 1-second delay between requests
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for non-2xx responses
        data = response.json()
        file_types = ["." + 
            file["key"].split(".")[-1].lower()
            for file in data.get("files", [])
            if "." in file["key"]
        ]

        return " * ".join(sorted(list(set(file_types)))) if file_types else None
    except Exception as e:
        print(f"Error fetching file formats for record ID {record_id}: {e}")
        return None

# Function to process a single URL or a list of URLs
def process_links(link_input):
    if isinstance(link_input, str):
        # Single URL case
        record_id = extract_zenodo_record_id(link_input)
        if record_id:
            return fetch_file_formats(record_id)
    elif isinstance(link_input, list):
        # List of URLs case
        for link in link_input:
            record_id = extract_zenodo_record_id(link.strip())
            if record_id:
                file_format = fetch_file_formats(record_id)
                if file_format:  # Return on first valid result
                    return file_format
    return None  # Return None if no valid formats are found


def update_fileformats(content, repository, file_path):
    """Update YAML content by adding author_with_orcid field.

    Parameters
    ----------
    content : dict
        Loaded YAML content.
    repository : str
        GitHub repository string (e.g., "org/repo").
    file_path : str
        Path to the YAML file in the repository.
    """
    modified = False
    do_exit = False
    for resource in content.get("resources", []):
        if "file_formats" not in resource:
            urls = resource.get("url", [])
            if isinstance(urls, str):
                urls = [urls]
            for url in urls:
                if url.startswith("https://zenodo.org/record") or url.startswith("https://zenodo.org/doi"):
                    try:
                        resource["file_formats"] = fetch_file_formats(extract_zenodo_record_id(url))
                        modified = True
                        break
                    except Exception as e:
                        print(f"Error fetching file formats for URL {url}: {e}")
                        if "TOO MANY REQUESTS" in str(e):
                            print("Too many requests, skipping this URL")
                            do_exit = True
                            break
            if do_exit:
                break
    if modified:
        main_branch = "main"
        new_branch = create_branch(repository, parent_branch=main_branch)
        new_content = yaml.dump(content, sort_keys=False, allow_unicode=True)
        write_file(repository, new_branch, file_path, new_content, "Add file formats to resources")
        pr_url = send_pull_request(
            repository,
            new_branch,
            "Add file formats",
            f"This PR adds file formats to resources YAML file."
        )
        print(pr_url)

if __name__ == "__main__":
    import sys
    repository = sys.argv[1]
    file_path = "resources/nfdi4bioimage.yml"

    # Authenticate and fetch file content
    repo = get_github_repository(repository)
    main_branch = "main"
    file_content = repo.get_contents(file_path, ref=main_branch)
    content = yaml.safe_load(file_content.decoded_content.decode())

    # Update YAML content
    update_fileformats(content, repository, file_path)
