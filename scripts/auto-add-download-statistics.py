# This script is executed every Monday at 11 am to gather the download statistics of all zenodo entries in the yml files.
# It will create a csv-file with the download statistics
# and send a pull request with the csv-file

import sys
from _github_utilities import create_branch, write_file, send_pull_request
import yaml
import datetime 

def main():
    """
    Main function to run the script that:
    
    1. Reads a repository name from command-line arguments.
    2. Creates a new branch in the given repository.
    3. Summarizes download statistics from a specified directory.
    4. Saves the statistics to GitHub as a CSV file.
    """
    repository = sys.argv[1]

    # read "database"
    branch = create_branch(repository)

    #define directory path
    directory_path = './resources/'

    # summarize download statistics
    download_statistics = summarize_download_statistics(directory_path)

    #get current date
    date = datetime.datetime.now().strftime("%Y%m%d")
    filename = f'download_statistics/{date}.csv'

    # save back to github
    write_file(repository, branch, filename, download_statistics, "Add " + filename)
    res = send_pull_request(repository, branch, f"Add {filename}", "") 

    print("Done.", res)

def summarize_download_statistics(directory_path):
    """
    Summarizes download statistics from all zenodo entries listed in YAML files in a given directory.

    Parameters
    ----------
    directory_path : str
        The path to the directory containing the YAML files.

    Returns
    -------
    str
        The content of the created CSV file as a string.
    """
    
    #import statements
    import requests
    import json
    from generate_link_lists import read_zenodo, read_yaml_file, all_content
    import pandas as pd
    import os
    from pathlib import Path
    import datetime
    import re

    #collect all content in a list of dictionaries
    content = all_content(directory_path) 

    #create pandas Dataframe called download_statistics 
    download_statistics = pd.DataFrame()

    for entry in content['resources']:
        urls = entry['url']

        # Ensure 'urls' is a list
        if not isinstance(urls, list):
            urls = [urls]

        for url in urls:
            # If 'zenodo.org' is in the URL
            if 'zenodo.org' in url:
                # Check if it's a DOI-based URL
                if 'doi' in url:
                    # Extract the Zenodo record ID from the DOI
                    match = re.search(r'zenodo\.(\d+)', url)
                    if match:
                        record_id = match.group(1)
                        # Change the URL to 'records' format
                        url = f"https://zenodo.org/records/{record_id}"

                #extract meta data of records in zenodo
                zenodo = read_zenodo(url)

                if 'stats' in zenodo.keys():

                    # define row entry
                    row_entry = {'url':url,
                                'authors': '"' + " and ".join([a["name"] for a in zenodo["metadata"]["creators"]]) + '"',
                                'downloads': zenodo['stats']['downloads'], 
                                'unique_downloads': zenodo['stats']['unique_downloads'], 
                                'views': zenodo['stats']['views'], 
                                'unique_views': zenodo['stats']['unique_views'], 
                                'version_downloads': zenodo['stats']['version_downloads'], 
                                'version_unique_downloads': zenodo['stats']['version_unique_downloads'], 
                                'version_unique_views': zenodo['stats']['version_unique_views'], 
                                'version_views': zenodo['stats']['version_views']}

                    # Create a new DataFrame with the new row
                    df_entry = pd.DataFrame([row_entry])

                    # Concatenate the new DataFrame with the existing `download_statistics` DataFrame
                    download_statistics = pd.concat([download_statistics, df_entry], ignore_index=True)
                    #print(download_statistics)

    #get current date
    date = datetime.datetime.now().strftime("%Y%m%d")

    #create filename
    filename = f'download_statistics/{date}.csv'

    #save download_statistics to CSV file with the new filename
    directory = Path(filename).parent
    os.makedirs(directory, exist_ok=True)

    download_statistics.to_csv(filename, index=False)
    #return download_statistics

    with open(filename, 'r') as file:
        return file.read()

if __name__ == "__main__":
    main()
