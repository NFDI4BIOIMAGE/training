# This script is executed when a new issue is created on our github repository. 
# In case the issue text consists only of a single line starting like a zenodo link, 
# it will retrieve all important details from the zenodo record, add it to a yml file
# and send a pull-request
import sys
from _github_utilities import create_branch, get_file_in_repository, get_issue_body, write_file, send_pull_request
import yaml
from datetime import datetime

def main():
    """
    Main function to handle the process of retrieving Zenodo data and appending
    it to a YAML file in a GitHub repository.

    This function takes command-line arguments for the repository name and issue number,
    retrieves the issue body, checks if it's a valid Zenodo link, retrieves corresponding
    data, and appends it to a specified YAML file by creating a new branch and submitting
    a pull request.

    Returns
    -------
    None
    """
    repository = sys.argv[1]
    issue = int(sys.argv[2])
    
    yml_filename = "resources/nfdi4bioimage.yml"
    
    issue_text = get_issue_body(repository, issue)
    zenodo_urls = [line for line in issue_text.splitlines() if line.startswith("https://zenodo.org/records")]
    
    if not zenodo_urls:
        print(issue_text, " does not contain any zenodo link. I show myself out.")
        return

    # read "database"
    branch = create_branch(repository)
    file_content = get_file_in_repository(repository, branch, yml_filename).decoded_content.decode()
    print("yml file content length:", len(file_content))

    for zenodo_url in zenodo_urls:
        # read data from zenodo
        zenodo_data_dict = complete_zenodo_data(zenodo_url)
        zenodo_yml = "\n- " + yaml.dump(zenodo_data_dict).replace("\n", "\n  ")
        
        # add entry
        file_content += zenodo_yml
    
    # save back to github
    write_file(repository, branch, yml_filename, file_content, "Add multiple Zenodo entries")
    res = send_pull_request(repository, branch, "Add multiple Zenodo entries", f"closes #{issue}")

    print("Done.", res)
    

def complete_zenodo_data(zenodo_url):
    """
    Completes Zenodo data retrieval and structuring for inclusion in a YAML file.

    Parameters
    ----------
    zenodo_url : str
        The URL of the Zenodo record.

    Returns
    -------
    entry : dict
        A dictionary containing structured metadata and statistics
        fetched from the Zenodo record.
    """
    from generate_link_lists import read_zenodo, remove_html_tags
    zenodo_data = read_zenodo(zenodo_url)
    entry = {}
    urls = [zenodo_url]

    if 'doi_url' in zenodo_data.keys():
        doi_url = zenodo_data['doi_url']
        
        # Add DOI URL to the URLs list if it's not already there
        if doi_url not in urls:
            urls.append(doi_url)
    entry['url'] = urls
        
    if 'metadata' in zenodo_data.keys():
        metadata = zenodo_data['metadata']
        # Update entry with Zenodo metadata and statistics
        entry['name'] = metadata['title']
        if 'publication_date' in metadata.keys():
            entry['publication_date'] = metadata['publication_date']
        if 'description' in metadata.keys():
            entry['description'] = remove_html_tags(metadata['description'])
        if 'creators' in metadata.keys():
            creators = metadata['creators']
            entry['authors'] = [c['name'] for c in creators]
        if 'license' in metadata.keys():
            entry['license'] = metadata['license']['id']
    
    if 'stats'  in zenodo_data.keys():
        entry['num_downloads'] = zenodo_data['stats']['downloads']
    
    entry['submission_date'] = datetime.now().isoformat()

    return entry


if __name__ == "__main__":
    main()
