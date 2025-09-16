import yaml
from _github_utilities import get_github_repository, create_branch, write_file, send_pull_request
import requests

def fetch_authors_from_zenodo(record_url):
    """Fetch author names and ORCIDs from Zenodo REST API.

    Parameters
    ----------
    record_url : str
        A Zenodo record URL.

    Returns
    -------
    list of str
        Authors with or without ORCIDs.
    """
    zenodo_api_url = "https://zenodo.org/api/records/" + record_url.split("/")[-1].split(".")[-1]
    response = requests.get(zenodo_api_url)
    response.raise_for_status()
    data = response.json()

    authors = data.get("metadata", {}).get("creators", [])

    author_with_orcid = []
    for author in authors:
        name = author.get("name", "")
        if "," in name:
            name = name.split(",")[1].strip() + " " + name.split(",")[0].strip()

        if "orcid" in author:
            author_with_orcid.append(f"{name} https://orgid.org/{author['orcid']}")
        else:
            author_with_orcid.append(name)
    return author_with_orcid

def update_authors_with_orcid(content, repository, file_path):
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
    for resource in content.get("resources", []):
        if "author_with_orcid" not in resource:
            urls = resource.get("url", [])
            if isinstance(urls, str):
                urls = [urls]
            for url in urls:
                if url.startswith("https://zenodo.org/record") or url.startswith("https://zenodo.org/doi"):
                    try:
                        resource["author_with_orcid"] = fetch_authors_from_zenodo(url)
                        modified = True
                        break
                    except Exception as e:
                        print(f"Error fetching authors for URL {url}: {e}")
    if modified:
        main_branch = "main"
        new_branch = create_branch(repository, parent_branch=main_branch)
        new_content = yaml.dump(content, sort_keys=False, allow_unicode=True)
        write_file(repository, new_branch, file_path, new_content, "Add authors with ORCIDs to resources")
        pr_url = send_pull_request(
            repository,
            new_branch,
            "Add authors with ORCIDs",
            f"This PR adds authors with ORCIDs to resources YAML file."
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
    update_authors_with_orcid(content, repository, file_path)
