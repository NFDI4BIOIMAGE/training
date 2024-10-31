#summarize download statistics

#import statements
import requests
import json
from generate_link_lists import read_zenodo, read_yaml_file, all_content
import pandas as pd
import os
from pathlib import Path
import datetime
import re

#define directory path
directory_path = './resources/'

#directory where the current script is located
#current_dir = Path(__file__).parent

#define path to 'resources' directory relative to current script
#directory_path = current_dir.parent / 'resources'

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
