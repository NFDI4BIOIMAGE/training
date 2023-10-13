def main():

    import os
    from datetime import datetime

    supported_content_types = ['collection', 'video', 'slide', 'notebook', 'event', 'blog', 'book', 'publication', 'document', 'documentation']
    directory_path = 'resources/'
    
    # Iterate over all files in the directory and accumulate content
    content = {'resources':[]}
    for filename in os.listdir(directory_path):
        if filename.endswith('.yml'):
            print("Adding", filename)
            new_content = read_yaml_file(directory_path + filename)
            content['resources'] = content['resources'] + new_content['resources']
            print(content.keys())

    # Go through all supported content types and generate corresponding markdown files
    for supported_type in supported_content_types:
        all = find_type(content, supported_type)
        write_md(all, supported_type, f"docs/{supported_type}/readme.md")

    # Put summary statistics in the main page
    last_updated = datetime.now().strftime('%Y-%m-%d')
    number_of_links = len(content['resources'])
    readme_file = "docs/readme.md"

    replace_in_file(readme_file, "{last_updated}", str(last_updated))
    replace_in_file(readme_file, "{number_of_links}", str(number_of_links))


def replace_in_file(filename, to_replace, replacement):
    with open(readme_file, 'r') as file:
        file_contents = file.read()
    file_contents = file_contents.replace(to_replace, replacement)
    with open(readme_file, 'w') as file:
        file.write(file_contents)    

def read_yaml_file(filename):
    """Read a yaml file and return the content as dictionary of dictionaries"""
    import yaml
    with open(filename, 'r') as file:
        data = yaml.safe_load(file)
        return data

def find_type(content, content_type):
    """Takes a dictionary of resources, searches for resources of a given type and returns them as new dictionary."""
    result = {}
    print("Searching for", content_type)
    for c in content['resources']:
        try:
            if content_type in c['type']:
                print("* listing", c['name'])
                result[c['name']] = c
        except:
            raise Exception("Error parsing " + str(c))

    return result

def write_md(resources, title, filename):
    """Turns a list of resources into a markdown file that can be parsed by Jupyter Book"""
    
    with open(filename, 'w') as file:
        print("Printing items of ", title)
        file.write("# " + title + '\n')
        
        for name, properties in resources.items():
            print("* ", name)
            file.write("## " + name + '\n')
            if 'authors' in properties:
                authors = properties['authors']
                file.write(f"By {authors}\n")
            if 'publication_date' in properties:
                publication_date = properties['publication_date']
                file.write(f"Published {publication_date}")
            if 'license' in properties:
                license = properties['license']
                file.write(f"licensed {license}")
            file.write("\n\n")
            if 'description' in properties:
                description = properties['description']
                file.write(f"\n{description}\n")
            if 'tags' in properties:
                tags = properties['tags']
                if type(tags) is list:
                    tags = ",".join(tags)
                file.write(f"\nTags: {tags}\n")
            if 'url' in properties:
                url = properties['url']
                if type(url) is list:
                    for u in url:
                        file.write(f"\n[{u}]({u})\n")
                else:
                    file.write(f"\n[{url}]({url})\n")
            
            file.write(f"\n")

if __name__ == "__main__":
    main()
