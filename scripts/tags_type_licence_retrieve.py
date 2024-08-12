import yaml
import os

def load_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

def extract_tags(yaml_content):
    tags = set()
    for item in yaml_content.get('resources', []):
        if 'tags' in item:
            tags.update(item['tags'])
    return tags

def extract_licenses(yaml_content):
    licenses = set()
    for item in yaml_content.get('resources', []):
        if 'license' in item:
            license_field = item['license']
            if isinstance(license_field, list):
                licenses.update(license_field)
            else:
                licenses.add(license_field)
    return licenses

def extract_types(yaml_content):
    types = set()
    for item in yaml_content.get('resources', []):
        if 'type' in item:
            types.update(item['type'])
    return types

def collect_tags_licenses_and_types_from_files(directory):
    all_tags = set()
    all_licenses = set()
    all_types = set()
    if os.path.exists(directory):
        for file_name in os.listdir(directory):
            if file_name.endswith('.yaml') or file_name.endswith('.yml'):
                file_path = os.path.join(directory, file_name)
                yaml_content = load_yaml(file_path)
                all_tags.update(extract_tags(yaml_content))
                all_licenses.update(extract_licenses(yaml_content))
                all_types.update(extract_types(yaml_content))
    else:
        print(f"Directory {directory} does not exist.")
    return all_tags, all_licenses, all_types

def write_to_file(items, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for item in sorted(items):
            file.write(item + '\n')

def main():
    # Get the absolute paths
    resource_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resources'))
    tags_output_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'tags.txt'))
    licenses_output_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'licenses.txt'))
    types_output_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'types.txt'))
    
    unique_tags, unique_licenses, unique_types = collect_tags_licenses_and_types_from_files(resource_directory)
    
    if unique_tags:
        write_to_file(unique_tags, tags_output_file)
        print(f"Tags have been written to {tags_output_file}")
    else:
        print("No tags found or directory is empty.")
    
    if unique_licenses:
        write_to_file(unique_licenses, licenses_output_file)
        print(f"Licenses have been written to {licenses_output_file}")
    else:
        print("No licenses found or directory is empty.")
        
    if unique_types:
        write_to_file(unique_types, types_output_file)
        print(f"Types have been written to {types_output_file}")
    else:
        print("No types found or directory is empty.")

if __name__ == "__main__":
    main()
