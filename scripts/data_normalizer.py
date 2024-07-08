import os
import yaml
import requests

# URL to fetch SPDX license data
SPDX_LICENSE_LIST_URL = "https://spdx.org/licenses/licenses.json"

# Fetch SPDX licenses from the SPDX website
def fetch_spdx_licenses():
    response = requests.get(SPDX_LICENSE_LIST_URL)
    if response.status_code == 200:
        spdx_data = response.json()
        spdx_licenses = {license["licenseId"].lower().replace(" ", "-"): license["licenseId"] for license in spdx_data["licenses"]}
        spdx_licenses.update({license["name"].lower().replace(" ", "-"): license["licenseId"] for license in spdx_data["licenses"]})
        return spdx_licenses
    else:
        raise Exception("Failed to fetch SPDX licenses")

# Normalize a license name using the SPDX license list
def normalize_license(license_name, spdx_licenses):
    license_name_lower = license_name.lower().strip().replace(" ", "-")
    return spdx_licenses.get(license_name_lower, license_name_lower)

# Normalize a single field (authors, tags)
def normalize_field(field):
    if isinstance(field, list):
        return [item.strip().title() for item in field]
    else:
        return field.strip().title()

# Specifically handle normalization of 'type' to ensure all outputs are lists
def normalize_type(type):
    if isinstance(type, list):
        return [type_.strip().title() for type_ in type]
    else:
        return [type.strip().title()]

# Create a mapping for items (authors, tags) to a consistent format
def create_mapping(items):
    normalized_items = {}
    for item in items:
        normalized_item = item.strip()
        normalized_items[item.lower().strip()] = normalized_item
    return normalized_items

# Normalize author names
def normalize_author_name(name):
    # name = name.replace('\xE1', 'á').replace('\xE9', 'é').replace('\xED', 'í').replace('\xF3', 'ó').replace('\xFA', 'ú')  # Handling special characters
    parts = [part.strip() for part in name.split(',')]
    if len(parts) == 2:
        return f"{parts[1]} {parts[0]}"
    return name

# Normalize author names
def normalize_author_name(name):
    name = name.replace('\xE1', 'á').replace('\xE9', 'é').replace('\xED', 'í').replace('\xF3', 'ó').replace('\xFA', 'ú')  # Handling special characters
    parts = [part.strip() for part in name.split(',')]
    if len(parts) == 2:
        return f"{parts[1]} {parts[0]}"
    return name

# Normalize author names
def normalize_author_name(name):
    name = name.replace('\xE1', 'á').replace('\xE9', 'é').replace('\xED', 'í').replace('\xF3', 'ó').replace('\xFA', 'ú')  # Handling special characters
    parts = [part.strip() for part in name.split(',')]
    if len(parts) == 2:
        return f"{parts[1]} {parts[0]}"
    return name

# Normalize a list of authors
def normalize_author_list(authors):
    normalized_authors = []

    # Split by semicolon to handle Type 1 and Type 2
    if ';' in authors:
        author_names = authors.split(';')
    else:
        author_names = [authors]

    for author in author_names:
        author = author.strip()
        if ',' in author:
            subparts = [part.strip() for part in author.split(',')]
            if len(subparts) % 2 == 0:
                # Check if alternating pattern suggests Type 4
                is_type_4 = all(len(subparts[i].split()) == 1 and len(subparts[i + 1].split()) == 1 for i in range(0, len(subparts), 2))
                if is_type_4:
                    # Handle Type 4: "lastname, firstname, lastname, firstname"
                    for i in range(0, len(subparts), 2):
                        lastname = subparts[i].strip()
                        firstname = subparts[i + 1].strip()
                        normalized_authors.append(f"{firstname} {lastname}")
                    continue  # Skip to the next author in the list
            # Handle Type 3: "firstname lastname, firstname lastname"
            subparts = author.split(', ')
            if all(len(part.split()) == 2 for part in subparts):
                normalized_authors.extend(subparts)
            else:
                # Handle Type 1: "lastname, firstname"
                for subpart in subparts:
                    normalized_authors.append(normalize_author_name(subpart.strip()))
        else:
            # Handle Type 2: "firstname lastname"
            normalized_authors.append(author)

    return normalized_authors

# Normalize the license names, authors, type, and tags in the data
def normalize_data(data, spdx_licenses):
    all_authors = set()
    all_tags = set()
    all_type = set()

    # Collect all authors, types, and tags
    for item in data:
        if 'authors' in item:
            if isinstance(item['authors'], list):
                for author in item['authors']:
                    all_authors.update([a.strip() for a in author.split(';')])
            else:
                all_authors.update([a.strip() for a in item['authors'].split(';')])

        if 'tags' in item:
            if isinstance(item['tags'], list):
                all_tags.update(item['tags'])
            else:
                all_tags.add(item['tags'])

        if 'type' in item:
            if isinstance(item['type'], list):
                all_type.update(item['type'])
            else:
                all_type.add(item['type'])

    # Create a mapping for authors 
    author_mapping = create_mapping(all_authors)

    # Normalize data
    for item in data:
        # Normalize license
        if 'license' in item:
            if isinstance(item['license'], list):
                item['license'] = [normalize_license(license, spdx_licenses) for license in item['license']]
            else:
                item['license'] = normalize_license(item['license'], spdx_licenses)

        # Normalize authors
        if 'authors' in item:
            if isinstance(item['authors'], list):
                normalized_authors = []
                for author in item['authors']:
                    normalized_authors.extend(normalize_author_list(author))
                item['authors'] = normalized_authors
            else:
                item['authors'] = normalize_author_list(item['authors'])

        # Normalize tags
        if 'tags' in item:
            if isinstance(item['tags'], list):
                item['tags'] = [normalize_field(tag) for tag in item['tags']]
            else:
                item['tags'] = normalize_field(item['tags'])

        # Normalize types
        if 'type' in item:
            item['type'] = normalize_type(item['type'])

    return data

# Read data from a YAML file
def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Write data to a YAML file
def write_data_to_file(data, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as file:
        yaml.dump(data, file, sort_keys=False)

# Process a single file, normalize and overwrite it
def process_file(file_path, spdx_licenses):
    data = read_data_from_file(file_path)
    resources_data = data.get('resources', [])
    normalized_data = normalize_data(resources_data, spdx_licenses) 
    write_data_to_file({'resources': normalized_data}, file_path)
    print(f"Normalization complete. File saved as {file_path}")

# Got all the files in the resources and normalized them
def main():
    spdx_licenses = fetch_spdx_licenses()
    # Find the script path
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    resources_dir = os.path.join(base_dir, "resources")
    
    for filename in os.listdir(resources_dir):
        # Iterate only the .yml/.yaml files
        if filename.endswith(".yml") or filename.endswith(".yaml"):
            file_path = os.path.join(resources_dir, filename)
            process_file(file_path, spdx_licenses)

if __name__ == "__main__":
    main()



# Normalize the license names, authors, type and tags in the data
def normalize_data(data, spdx_licenses):
    all_authors = set()
    all_tags = set()
    all_type = set()

    # Collect all authors, types, and tags
    for item in data:
        if 'authors' in item:
            if isinstance(item['authors'], list):
                for author in item['authors']:
                    all_authors.update([a.strip() for a in author.split(';')])
            else:
                all_authors.update([a.strip() for a in item['authors'].split(';')])

        if 'tags' in item:
            if isinstance(item['tags'], list):
                all_tags.update(item['tags'])
            else:
                all_tags.add(item['tags'])

        if 'type' in item:
            if isinstance(item['type'], list):
                all_type.update(item['type'])
            else:
                all_type.add(item['type'])

    # Create a mapping for authors 
    author_mapping = create_mapping(all_authors)

    # Normalize data
    for item in data:
        # Normalize license
        if 'license' in item:
            if isinstance(item['license'], list):
                item['license'] = [normalize_license(license, spdx_licenses) for license in item['license']]
            else:
                item['license'] = normalize_license(item['license'], spdx_licenses)

        # Normalize authors
        if 'authors' in item:
            if isinstance(item['authors'], list):
                normalized_authors = []
                for author in item['authors']:
                    normalized_authors.extend(normalize_author_list(author))
                item['authors'] = normalized_authors
            else:
                item['authors'] = normalize_author_list(item['authors'])

        # Normalize tags
        if 'tags' in item:
            if isinstance(item['tags'], list):
                item['tags'] = [normalize_field(tag) for tag in item['tags']]
            else:
                item['tags'] = normalize_field(item['tags'])

        # Normalize types
        if 'type' in item:
            item['type'] = normalize_type(item['type'])

    return data

# Read data from a YAML file
def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Write data to a YAML file
def write_data_to_file(data, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as file:
        yaml.dump(data, file, sort_keys=False)

# Process a single file, normalize and overwrite it
def process_file(file_path, spdx_licenses):
    data = read_data_from_file(file_path)
    resources_data = data.get('resources', [])
    normalized_data = normalize_data(resources_data, spdx_licenses) 
    write_data_to_file({'resources': normalized_data}, file_path)
    print(f"Normalization complete. File saved as {file_path}")

# Got all the files in the resources and normalized them
def main():
    spdx_licenses = fetch_spdx_licenses()
    # Find the script path
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    resources_dir = os.path.join(base_dir, "resources")
    
    for filename in os.listdir(resources_dir):
        # Iterate only the .yml/.yaml files
        if filename.endswith(".yml") or filename.endswith(".yaml"):
            file_path = os.path.join(resources_dir, filename)
            process_file(file_path, spdx_licenses)

if __name__ == "__main__":
    main()
