def main():

    import os
    from datetime import datetime

    directory_path = 'resources/'
    toc_file = "docs/_toc.yml"
    readme_file = "docs/readme.md"
    MINIMUM_ITEM_COUNT = 5
    
    # Iterate over all files in the directory and accumulate content
    content = {'resources':[]}
    for filename in os.listdir(directory_path):
        if filename.endswith('.yml'):
            print("Adding", filename)
            new_content = read_yaml_file(directory_path + filename)
            content['resources'] = content['resources'] + new_content['resources']
            print(content.keys())

    # Go through all supported content types and generate corresponding markdown files
    all_content_types = collect_all_content_types(content)
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
    all_tag_counts = collect_all_tags(content)
    tag_toc = ""
    for tag in sorted(list(all_tag_counts.keys())):
        count = all_tag_counts[tag] 
        if count >= MINIMUM_ITEM_COUNT:
            selected_content = find_tag(content, tag)
            filename = "tags/" + tag.replace(" ", "_")
            write_md(selected_content, tag, "docs/" + filename + ".md")
            tag_toc += "    - file: " + filename + "\n"    
    replace_in_file(toc_file, "{tag_toc}", tag_toc)
    
    # Put summary statistics in the main page
    last_updated = datetime.now().strftime('%Y-%m-%d')
    number_of_links = len(content['resources'])

    replace_in_file(readme_file, "{last_updated}", str(last_updated))
    replace_in_file(readme_file, "{number_of_links}", str(number_of_links))


def replace_in_file(filename, to_replace, replacement):
    with open(filename, 'r') as file:
        file_contents = file.read()
    file_contents = file_contents.replace(to_replace, replacement)
    with open(filename, 'w') as file:
        file.write(file_contents)    


def read_yaml_file(filename):
    """Read a yaml file and return the content as dictionary of dictionaries"""
    import yaml
    with open(filename, 'r') as file:
        data = yaml.safe_load(file)
        return data


def collect_all_content_types(content):
    return collect_all(content, "type")


def collect_all_tags(content):
    return collect_all(content, "tags")


def collect_all(content, what_to_collect):
    all_tags = {}
    for c in content['resources']:
        if what_to_collect in c:
            tags = c[what_to_collect]
            if type(tags) is not list and "," in tags:
                tags = tags.split(",")
            if type(tags) is not list:
                tags = [tags]

            for tag in tags:
                tag = tag.lower()
                if tag not in all_tags.keys():
                    all_tags[tag] = 1
                else:
                    all_tags[tag] += 1
    return all_tags

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
                if type(list_to_look_at) is not list:
                    list_to_look_at = [list_to_look_at]
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
                file.write(f"\nBy {authors}\n")
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
                file.write(f"Tags: {tags}\n")
            if 'url' in properties:
                url = properties['url']
                if type(url) is list:
                    for u in url:
                        file.write(f"\n[{u}]({u})\n")
                else:
                    file.write(f"\n[{url}]({url})\n")
            
            file.write(f"---\n")

if __name__ == "__main__":
    main()
