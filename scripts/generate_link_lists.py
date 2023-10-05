def main():

    import os

    supported_content_types = ['collection', 'video', 'slide', 'notebook', 'event', 'blog', 'book', 'publication']
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
        if content_type in c['type']:
            print("* listing", c['name'])
            result[c['name']] = c
    return result

def write_md(resources, content_type_name, filename):
    """Turns a list of resources into a markdown file that can be parsed by Jupyter Book"""
    
    with open(filename, 'w') as file:

        file.write("# " + content_type_name + '\n')
        
        for name, properties in resources.items():
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
                tags = str(properties['tags'])
                file.write(f"\nTags: {tags}\n")
            if 'url' in properties:
                url = properties['url']
                file.write(f"\n[{url}]({url})\n")
            
            file.write(f"\n")

if __name__ == "__main__":
    main()