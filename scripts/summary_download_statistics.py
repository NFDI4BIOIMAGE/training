#summarize download statistics

#import statements
import requests
import json
from generate_link_lists import read_zenodo, read_yaml_file, all_content
import pandas as pd
from pathlib import Path

#define directory path
directory_path = 'resources/'

#directory where the current script is located
#current_dir = Path(__file__).parent

#define path to 'resources' directory relative to current script
#directory_path = current_dir.parent / 'resources'

#collect all content in a list of dictionaries
content = all_content(directory_path) 

#create pandas Dataframe called download_statistics 
download_statistics = pd.DataFrame(columns=['file_id', 'downloads', 'unique_downloads', 'views', 'unique_views', 'version_downloads', 'version_unique_downloads', 'version_unique_views', 'version_views'])

for entry in content['resources']:
    urls = entry['url']

    #make urls a list if it is not already
    if not type(urls) is list:
            urls = [urls]
    
    for url in urls:
        # if zenodo in url
        if 'zenodo.org' in url:

            #extract meta data of records in zenodo
            zenodo = read_zenodo(url)

            if 'stats' in zenodo.keys():
                
                #zenodo metadata download statistics stored on per-file basis, so we need to access all files in the record using 'id' key
                for file in zenodo['files']:

                    # define row entry
                    row_entry = {'file_id': file['id'], 'downloads': zenodo['stats']['downloads'], 'unique_downloads': zenodo['stats']['unique_downloads'], 'views': zenodo['stats']['views'], 'unique_views': zenodo['stats']['unique_views'], 'version_downloads': zenodo['stats']['version_downloads'], 'version_unique_downloads': zenodo['stats']['version_unique_downloads'], 'version_unique_views': zenodo['stats']['version_unique_views'], 'version_views': zenodo['stats']['version_views']}

                    # Create a new DataFrame with the new row
                    df_entry = pd.DataFrame([row_entry])

                    # Concatenate the new DataFrame with the existing `download_statistics` DataFrame
                    download_statistics = pd.concat([download_statistics, df_entry], ignore_index=True)
                    print(download_statistics)


download_statistics.to_csv('download_statistics.csv', index=False)