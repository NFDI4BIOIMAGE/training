def main():

    import os

    supported_content_types = ['collection', 'video']
    directory_path = 'resources/'
    
    # Iterate over all files in the directory and accumulate content
    content = {}
    for filename in os.listdir(directory_path):
        if filename.endswith('.yml'):
            new_content = read_yaml_file(directory_path + filename)
            content.update(new_content)    

    # Go through all supported content types and generate corresponding markdown files
    for supported_type in supported_content_types:
        all = find_type(content, supported_type)
        write_md(all, supported_type, f"docs/{supported_type}/readme.md")


def read_yaml_file(filename):
    """Read a yaml file and return the content as dictionary of dictionaries"""
    import yaml
    with open(filename, 'r') as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as exc:
            print(exc)
            return None

def find_type(content, content_type):
    """Takes a dictionary of resources, searches for resources of a given type and returns them as new dictionary."""
    result = {}
    for c in content['resources']:
        if content_type in c['type']:
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
                file.write(f"By: {authors}\n")
            if 'publication_date' in properties:
                publication_date = properties['publication_date']
                file.write(f"Published {publication_date}\n")
            if 'url' in properties:
                url = properties['url']
                file.write(f"[{url}]({url})\n")
            if 'description' in properties:
                description = properties['description']
                file.write(f"{description}\n")
            file.write(f"\n")

if __name__ == "__main__":
    main()