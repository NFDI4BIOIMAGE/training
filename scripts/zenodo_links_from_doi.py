#store zenodo links from doi

import requests
import json
from generate_link_lists import read_doi, all_content

#define directory path
directory_path = '../resources/'

#collect all content in a list of dictionaries
content = all_content(directory_path) 

for entry in content['resources']:
    urls = entry['url']

    #make urls a list if it is not already
    if not type(urls) is list:
            urls = [urls]
            #print(urls)
    
    for url in urls:
        
        if 'doi.org' in url:

            #extract meta data of records from doi.org
            data = read_doi(url)
            
            #search for word zenodo in meta data because this is the zenodo-link we want to append to url
            if 'zenodo.org' in str(data['values']):

                 #check if zenodo is already in url
                 if 'zenodo' in url:
    
                    #replace zenodo link with the new one but keep all other links
                    entry['url'].remove(url)
                    entry['url'].append(data['values'][1]['data']['value'])
                    print(entry['url'])