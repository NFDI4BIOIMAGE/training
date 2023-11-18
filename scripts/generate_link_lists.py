def main():

    import os
    from datetime import datetime

    directory_path = 'resources/'
    toc_file = "docs/_toc.yml"
    readme_file = "docs/readme.md"
    MINIMUM_ITEM_COUNT = 5
    
    # Iterate over all files in the directory and accumulate content
    content = all_content(directory_path)

    # Go through all supported content types and generate corresponding markdown files
    all_content_types = collect_all(content, "type")
    type_toc = ""
    for supported_type in sorted(list(all_content_types.keys())):
        count = all_content_types[supported_type] 
        if count >= MINIMUM_ITEM_COUNT:
            all = find_type(content, supported_type)
            filename = "content_types/" + supported_type
            write_md(all, supported_type, "docs/" + filename + ".md")
            type_toc = type_toc + "    - file: " + filename + "\n"
    replace_in_file(toc_file, "{type_toc}", type_toc)

    # go through all tags and generate corresponding markdown files
    all_tag_counts = collect_all(content, "tags")
    tag_toc = ""
    for tag in sorted(list(all_tag_counts.keys())):
        count = all_tag_counts[tag] 
        if count >= MINIMUM_ITEM_COUNT:
            selected_content = find_tag(content, tag)
            filename = "tags/" + tag.replace(" ", "_")
            write_md(selected_content, tag, "docs/" + filename + ".md")
            tag_toc += "    - file: " + filename + "\n"    
    replace_in_file(toc_file, "{tag_toc}", tag_toc)

    # go through all licenses and generate corresponding markdown files
    all_license_counts = collect_all(content, "license")
    license_toc = ""
    for license in sorted(list(all_license_counts.keys())):
        count = all_license_counts[license] 
        if count >= MINIMUM_ITEM_COUNT:
            selected_content = find_license(content, license)
            filename = "licenses/" + license.replace(" ", "_")
            write_md(selected_content, license, "docs/" + filename + ".md")
            license_toc += "    - file: " + filename + "\n"    
    replace_in_file(toc_file, "{license_toc}", license_toc)

    # go through all authors and generate corresponding markdown files
    all_author_counts = collect_all(content, "authors")
    author_toc = ""
    for author in sorted(list(all_author_counts.keys())):
        count = all_author_counts[author] 
        print("AAACC", author, count)
        if count >= MINIMUM_ITEM_COUNT:
            selected_content = find_author(content, author)
            filename = "authors/" + author.replace(" ", "_")
            write_md(selected_content, author, "docs/" + filename + ".md")
            author_toc += "    - file: " + filename + "\n"    
    replace_in_file(toc_file, "{author_toc}", author_toc)

    # go through all urls and detect duplicates
    all_urls = collect_all(content, "url")
    duplicate_found = False
    for url, count in all_urls.items():
        if count > 1:
            print(f"Duplicate entry detected: {url}")
            duplicate_found = True
    if duplicate_found:
        raise KeyError(f"Duplicate entries detected! Remove them and rebuild the index.")
    
    # Put summary statistics in the main page
    last_updated = datetime.now().strftime('%Y-%m-%d')
    number_of_links = len(content['resources'])

    replace_in_file(readme_file, "{last_updated}", str(last_updated))
    replace_in_file(readme_file, "{number_of_links}", str(number_of_links))

def all_content(directory_path):
    import os
    content = {'resources':[]}
    for filename in os.listdir(directory_path):
        if filename.endswith('.yml'):
            print("Adding", filename)
            new_content = read_yaml_file(directory_path + filename)
            content['resources'] = content['resources'] + new_content['resources']
            # print(content.keys())
    return content

def load_dataframe(directory_path):
    import pandas as pd
    content = all_content(directory_path)
    return pd.DataFrame(content['resources'])

def replace_in_file(filename, to_replace, replacement):
    with open(filename, 'r') as file:
        file_contents = file.read()
    file_contents = file_contents.replace(to_replace, replacement)
    with open(filename, 'w') as file:
        file.write(file_contents)    


def read_yaml_file(filename):
    """Read a yaml file and return the content as dictionary of dictionaries"""
    import yaml
    with open(filename, 'r', encoding="utf8") as file:
        data = yaml.safe_load(file)
        return data

def write_yaml_file(file_path, data):
    """Saves data as yaml file to disk"""
    import yaml
    with open(file_path, 'w') as file:
        yaml.dump(data, file)


def update_all_yaml_files(directory_path):
    import os
    for filename in os.listdir(directory_path):
        if filename.endswith('.yml'):
            print("updating", filename)
            update_yaml_file(directory_path + filename)


def update_yaml_file(yaml_filename):
    """
    Update the YAML file with Zenodo metadata and statistics.
    
    Parameters:
    - yaml_filename : str
        The filename of the YAML file.
    """
    # Read the content from the YAML file
    content = read_yaml_file(yaml_filename)
    entries = content['resources']
    
    # Iterate over each entry in the YAML file
    for entry in entries:
        urls = entry['url']
        if not type(urls) is list:
            urls = [urls]
    
        # Check each URL and extract the Zenodo and DOI URLs
        doi_url = None
        zenodo_url = None
        for url in urls:
            url = url.strip()
            if url.startswith('https://zenodo.org/'):
                zenodo_url = url
            if url.startswith('https://doi.org/'):
                doi_url = url
    
        # If Zenodo URL is found, fetch the metadata and update the entry
        if zenodo_url is not None:
            zenodo_data = read_zenodo(zenodo_url)

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
                    entry['authors'] = ", ".join([c['name'] for c in creators])
                if 'license' in metadata.keys():
                    entry['license'] = metadata['license']['id'].replace("-", " ")
            
            if 'stats'  in zenodo_data.keys():
                entry['num_downloads'] = zenodo_data['stats']['downloads']
    
    # Write the modified content back to the YAML file
    write_yaml_file(yaml_filename, content)
    

def read_doi(doi):
    import requests
    import json

    doi = doi.replace("https://doi.org/", "")
    url = "https://doi.org/api/handles/" + doi
    
    # Download the file
    response = requests.get(url)
    data = response.json()
    return data


def read_zenodo(record):
    
    import requests
    import json

    record = record.replace("https://zenodo.org/", "")
    url = "https://zenodo.org/api/" + record
    
    # Download the file
    response = requests.get(url)
    data = response.json()
    return data


def remove_html_tags(text):
    import re
    cleaned_text = re.sub('<.*?>', '', text)
    return cleaned_text
    

def collect_all(content, what_to_collect):
    all_tags = {}
    for c in content['resources']:
        if what_to_collect in c:
            tags = c[what_to_collect]
            if type(tags) is not list and "," in tags:
                tags = tags.split(",")
                tags = [t.strip() for t in tags]
            if type(tags) is not list:
                tags = [tags]

            for tag in tags:
                tag = tag.lower().strip()
                if tag not in all_tags.keys():
                    all_tags[tag] = 1
                else:
                    all_tags[tag] += 1
    return all_tags


def find_author(content, author):
    """Takes a dictionary of resources, searches for resources of a given author and returns them as new dictionary."""
    return find_anything(content, "authors", author)
    
def find_license(content, license):
    """Takes a dictionary of resources, searches for resources of a given license and returns them as new dictionary."""
    return find_anything(content, "license", license)

def find_type(content, content_type):
    """Takes a dictionary of resources, searches for resources of a given type and returns them as new dictionary."""
    return find_anything(content, "type", content_type)

def find_tag(content, tag):
    """Takes a dictionary of resources, searches for resources which have a given tag and returns them as new dictionary."""
    return find_anything(content, "tags", tag)

def find_anything(content, what_to_look_in, what_to_find):
    result = {}
    print("Searching for", what_to_look_in, "=", what_to_find)
    for c in content['resources']:
        if what_to_look_in in c:
            try:
                list_to_look_at = c[what_to_look_in]
                if type(list_to_look_at) is not list and "," in list_to_look_at:
                    list_to_look_at = list_to_look_at.split(",")
                    list_to_look_at = [t.strip() for t in list_to_look_at]
                if type(list_to_look_at) is not list:
                    list_to_look_at = [list_to_look_at]

                list_to_look_at = [str(i).lower().strip() for i in list_to_look_at]
                if what_to_find in list_to_look_at:
                    print("* listing", c['name'])
                    result[c['name']] = c
            except:
                raise Exception("Error parsing " + str(c))

    return result

def write_md(resources, title, filename):
    """Turns a list of resources into a markdown file that can be parsed by Jupyter Book"""
    
    with open(filename, 'w') as file:
        print("Printing items of ", title)

        num_items = len(resources.keys())

        title = title[0].upper() + title[1:]
        
        file.write(f"# {title} ({num_items})\n")

        for name in sorted(list(resources.keys())):
            properties = resources[name]
            
            print("* ", name)
            file.write("## " + name + '\n')
            if 'authors' in properties:
                authors = properties['authors']
                file.write(f"\n{authors}\n")
            if 'publication_date' in properties:
                publication_date = properties['publication_date']
                file.write(f"\nPublished {publication_date}\n")
            if 'license' in properties:
                license = properties['license']
                file.write(f"\nLicensed {license}\n")
            file.write("\n\n")
            if 'description' in properties:
                description = properties['description']
                file.write(f"\n{description}\n")
            if 'tags' in properties:
                tags = properties['tags']
                if type(tags) is list:
                    tags = ", ".join(tags)
                file.write(f"\nTags: {tags}\n")
            if 'type' in properties:
                content_type = properties['type']
                if type(content_type) is list:
                    content_type = ", ".join(content_type)
                file.write(f"\nContent type: {content_type}\n")
            if 'url' in properties:
                url = properties['url']
                if type(url) is list:
                    for u in url:
                        file.write(f"\n[{u}]({u})\n")
                else:
                    file.write(f"\n[{url}]({url})\n")
            
            file.write(f"\n\n---\n\n")

if __name__ == "__main__":
    main()
