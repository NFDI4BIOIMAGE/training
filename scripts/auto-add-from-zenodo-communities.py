# This script is executed when a new issue is created on our github repository. 
# In case the issue text consists only of a single line starting like a zenodo link, 
# it will retrieve all important details from the zenodo record, add it to a yml file
# and send a pull-request
import sys
from _github_utilities import create_branch, get_file_in_repository, get_issue_body, write_file, send_pull_request
import yaml
import os
import requests
import bia_bob
import shutil
import pandas as pd
from generate_link_lists import load_dataframe, update_yaml_file, complete_zenodo_data
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

    token = os.getenv('ZENODO_API_KEY')
    communities = ['nfdi4bioimage', 'gerbi', 'euro-bioimaging', 'neubias', 'bio-formats', 'globias']

    yml_filename = "resources/nfdi4bioimage.yml"

    # read "database"
    branch = create_branch(repository)
    print("New branch:", branch)
    log = []
    new_data = []

    # old data
    df = load_dataframe("resources/")
    all_urls = str(df["url"].tolist())

    for community in communities:
        log.append(f"# {community}")
        log.append(f"https://zenodo.org/communities/{community}")
        # new data
        response = requests.get('https://zenodo.org/api/records',
                                params={'communities': community,
                                        'access_token': token})
        online_data = response.json()
        hits = online_data["hits"]["hits"]
        urls = [u["links"]["self_html"] for u in hits]


        # compare which new is not in old

        for url in urls:
            print(url)
            data = complete_zenodo_data(url)

            if isinstance(data["url"], str):
                data["url"] = [data["url"]]

            not_in_data_yet = True
            for u in data["url"]:
                if u in all_urls:
                    not_in_data_yet = False

            if not_in_data_yet:
                data['added_date'] = datetime.now().isoformat()
                name = data["name"]
                log.append(f"* [{name}]({url})")
                new_data.append(data)

                # deal with entries listed in multiple communities
                all_urls = all_urls + "\n" + "\n".join([u for u in data["url"]])

    import yaml
    zenodo_yml = yaml.dump(new_data) #.replace("\n", "\n  ")
    #print(zenodo_yml)

    # save data in repository
    file_content = get_file_in_repository(repository, branch, yml_filename).decoded_content.decode()
    print("yml file content length:", len(file_content))

    # add entry
    file_content += zenodo_yml
    #print("zenodo_yml", len(zenodo_yml))

    # save back to github
    write_file(repository, branch, yml_filename, file_content, "Add entries from " + ", ".join(communities))

    log = "\n".join(log)
    res = send_pull_request(repository, branch, "Add content from communities: " + ", ".join(communities), f"Added contents:\n{log}")

    print("Done.", res)
    



if __name__ == "__main__":
    main()
