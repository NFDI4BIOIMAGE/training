#summarize download statistics

#import statements
import requests
import json
from generate_link_lists import read_zenodo, read_yaml_file, all_content
import pandas as pd

#define directory path
directory_path = '../resources/'

#collect all content in a list of dictionaries
content = all_content(directory_path) 

#create pandas Dataframe called download_statistics 
download_statistics = pd.DataFrame(columns=['doi_url', 'downloads', 'unique_downloads', 'views', 'unique_views', 'version_downloads', 'version_unique_downloads', 'version_unique_views', 'version_views'])

for entry in content['resources']:

    # if zenodo in url
    if 'zenodo.org' in str(entry['url']):

        #extract meta data of records in zenodo
        zenodo = read_zenodo(str(entry['url']))
        if 'stats' in zenodo.keys():
            print(zenodo)
            
            #create new row entry
            row_entry = {'doi_url': zenodo['doi_url'], 'downloads': zenodo['stats']['downloads'], 'unique_downloads': zenodo['stats']['unique_downloads'], 'views': zenodo['stats']['views'], 'unique_views': zenodo['stats']['unique_views'], 'version_downloads': zenodo['stats']['version_downloads'], 'version_unique_downloads': zenodo['stats']['version_unique_downloads'], 'version_unique_views': zenodo['stats']['version_unique_views'], 'version_views': zenodo['stats']['version_views']}

            # Create a data frame with the new row entry
            df_entry = pd.DataFrame([row_entry])

            #concatenate the new DataFrame with the existing `download_statistics` DataFrame
            download_statistics = pd.concat([download_statistics, df_entry], ignore_index=True)
        
#save pd dataframe as csv file
download_statistics.to_csv('download_statistics.csv', index=False)