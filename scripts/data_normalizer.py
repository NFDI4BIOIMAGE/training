import os
import re
import yaml
import requests

# URL to fetch license data in JSON format
SPDX_LICENSE_LIST_URL = "https://spdx.org/licenses/licenses.json"

# Define a normalization mapping for specific terms
normalization_mapping = {
    "Bsd 2-Clause": "BSD-2-Clause",
    "Bsd-2-Clause": "BSD-2-Clause",
    "Bsd 3-Clause": "BSD-3-Clause",
    "Bsd-3-Clause": "BSD-3-Clause",
    "Cc By 4.0": "CC-BY-4.0",
    "Cc-By 4.0": "CC-BY-4.0",
    "Cc-By-4.0": "CC-BY-4.0",
    "Creative Commons / Attribution 4.0 International (CC BY 4.0)": "CC-BY-4.0",
    "Creative Commons Attribution 4.0 International": "CC-BY-4.0",
    "CC0 licence (some accessions are available under different license, if so the license is indicated as attribute on dataset)": "CC0-1.0",
    "CC0": "CC0-1.0",
    "Bio-Image Analysis": "Bioimage Analysis",
    "Omero": "OMERO",
    "Fair-Principles": "FAIR-Principles",
    "Meta Data": "Metadata",
    "cc-by-4.0": "CC-BY-4.0",
    "Unclear": "Unknown"
    # Add more mappings as needed
}


def fetch_spdx_licenses():
    """
    Fetches and processes license data from the provided URL.

    This function retrieves license information in JSON format from the specified URL,
    processes it, and returns a dictionary with normalized keys for easy lookup.

    Returns:
        dict: A dictionary with license names as keys and their IDs as values.

    Raises:
        Exception: If the licenses cannot be fetched.
    """
    response = requests.get(SPDX_LICENSE_LIST_URL)
    if response.status_code == 200:
        spdx_data = response.json()
        spdx_licenses = {license["licenseId"].lower().replace(" ", "-"): license["licenseId"] for license in spdx_data["licenses"]}
        spdx_licenses.update({license["name"].lower().replace(" ", "-"): license["licenseId"] for license in spdx_data["licenses"]})
        return spdx_licenses
    else:
        raise Exception("Failed to fetch SPDX licenses")

def normalize_license(license_name, spdx_licenses):
    """
    Normalizes a license name and converts it to uppercase.

    Args:
        license_name (str): The name of the license to be normalized.
        spdx_licenses (dict): A dictionary of available licenses.

    Returns:
        str: The normalized license name in uppercase.
    """
    # Apply the normalization mapping first
    license_name = normalization_mapping.get(license_name, license_name)
    
    # Normalize the license name to match SPDX format
    license_name_lower = license_name.lower().strip().replace(" ", "-")
    
    # Get the normalized license from SPDX list or keep the original
    normalized_license = spdx_licenses.get(license_name_lower, license_name)
    
    # Convert the normalized license to uppercase
    return normalized_license.upper()


def normalize_field(field):
    """
    Normalizes a single field (authors, tags) by applying specific mappings.

    Args:
        field (str or list): The field to be normalized.

    Returns:
        str or list: The normalized field.
    """
    if isinstance(field, list):
        return [normalization_mapping.get(item.strip().title(), item.strip().title()) for item in field]
    else:
        return normalization_mapping.get(field.strip().title(), field.strip().title())

# Apply normalize_field to each field in the normalize_data function


def normalize_type(type):
    """
    Specifically handles normalization of 'type' to ensure all outputs are lists.

    Args:
        type (str or list): The 'type' field to be normalized.

    Returns:
        list: The normalized 'type' field.
    """
    if isinstance(type, list):
        return [type_.strip().title() for type_ in type]
    else:
        return [type.strip().title()]

def create_mapping(items):
    """
    Creates a mapping for items (authors, tags) to a consistent format.

    This function takes a list of items, normalizes each item by stripping any leading
    or trailing whitespace, and then creates a dictionary where the keys are the
    normalized (lowercase and stripped) versions of the items, and the values are
    the original, stripped items.

    Args:
        items (list): The items to be mapped.

    Returns:
        dict: A dictionary containing the normalized items.
    """
    normalized_items = {}
    for item in items:
        normalized_item = item.strip()
        normalized_items[item.lower().strip()] = normalized_item
    return normalized_items

def normalize_author_name(name):
    """
    Normalizes an author name.

    Args:
        name (str): The author name to be normalized.

    Returns:
        str: The normalized author name.
    """
    parts = [part.strip() for part in name.split(',')]
    if len(parts) == 2:
        return f"{parts[1]} {parts[0]}"
    return name

def normalize_author_list(authors):
    """
    Normalize a list of author names from various formats into a standardized format.

    This function takes a string of author names, which can be in different formats,
    and normalizes them into a consistent "Firstname Lastname" format. The input
    string can contain multiple authors separated by semicolons.

    Args:
        authors (str): The authors to be normalized. The authors can be in formats 
        like "Lastname, Firstname", "Lastname, Firstname, Lastname, Firstname", 
        "Firstname Lastname", or combinations thereof.

    Returns:
        list: A list of normalized author names in the format "Firstname Lastname".
    """
    normalized_authors = []

    # Split the authors string by ';' if it contains multiple authors
    if ';' in authors:
        author_names = authors.split(';')
    else:
        author_names = [authors]

    # Process each author name
    for author in author_names:
        author = author.strip()

        # Check if the author name contains a comma, indicating "Lastname, Firstname" format
        if ',' in author:
            subparts = [part.strip() for part in author.split(',')]

            # Handle special case: "Lastname, Firstname, Lastname, Firstname" format
            if len(subparts) % 2 == 0:
                is_type_4 = all(len(subparts[i].split()) == 1 and len(subparts[i + 1].split()) == 1 for i in range(0, len(subparts), 2))
                if is_type_4:
                    for i in range(0, len(subparts), 2):
                        lastname = subparts[i].strip()
                        firstname = subparts[i + 1].strip()
                        normalized_authors.append(f"{firstname} {lastname}")
                    continue

            # Handle case: "Lastname, Firstname" or "Lastname, Firstname, Lastname, Firstname"
            subparts = author.split(', ')
            if all(len(part.split()) == 2 for part in subparts):
                normalized_authors.extend(subparts)
            else:
                # Handle case where there might be multiple parts with different formats
                for subpart in subparts:
                    normalized_authors.append(normalize_author_name(subpart.strip()))
        else:
            # Handle case: "Firstname Lastname" format
            normalized_authors.append(author)

    return normalized_authors

def normalize_description_date_time(description):
    """
    Normalizes a date/time string by removing unwanted Unicode characters and ensuring the format is correct.

    Args:
        description (str): The description containing the date/time.

    Returns:
        str: The normalized date/time string.
    """
    # Remove unwanted Unicode characters
    normalized_description = re.sub(r'\xE2\u20AC\xAF', '', description)
    
    # Add a space between time and AM/PM if not present
    normalized_description = re.sub(r'(\d)(AM|PM)', r'\1 \2', normalized_description)

    return normalized_description 

def normalize_data(data, spdx_licenses):
    """
    Normalizes the license names, authors, type, and tags in the data.

    Args:
        data (list): The data to be normalized.
        spdx_licenses (dict): A dictionary containing the SPDX licenses.

    Returns:
        list: The normalized data.
    """
    all_authors = set()
    all_tags = set()
    all_type = set()

    # Collect all unique authors, tags, and types from the dataset
    for item in data:
        if 'authors' in item and item['authors'] is not None:
            if isinstance(item['authors'], list):
                for author in item['authors']:
                    all_authors.update([a.strip() for a in author.split(';')])
            else:
                all_authors.update([a.strip() for a in item['authors'].split(';')])

        if 'tags' in item and item['tags'] is not None:
            if isinstance(item['tags'], list):
                all_tags.update(item['tags'])
            else:
                all_tags.add(item['tags'])

        if 'type' in item and item['type'] is not None:
            if isinstance(item['type'], list):
                all_type.update(item['type'])
            else:
                all_type.add(item['type'])

    # Create mappings for authors to ensure consistent format
    author_mapping = create_mapping(all_authors)

    # Normalize each field in the dataset
    for item in data:
        if 'license' in item and item['license'] is not None:
            if isinstance(item['license'], list):
                item['license'] = [normalize_license(license, spdx_licenses) for license in item['license']]
            else:
                item['license'] = normalize_license(item['license'], spdx_licenses)

        if 'authors' in item and item['authors'] is not None:
            if isinstance(item['authors'], list):
                normalized_authors = []
                for author in item['authors']:
                    # Use author_mapping for consistency
                    normalized_author = author_mapping.get(author.lower().strip(), author)
                    normalized_authors.extend(normalize_author_list(normalized_author))
                item['authors'] = normalized_authors
            else:
                # Use author_mapping for single author
                normalized_author = author_mapping.get(item['authors'].lower().strip(), item['authors'])
                item['authors'] = normalize_author_list(normalized_author)

        if 'tags' in item and item['tags'] is not None:
            if isinstance(item['tags'], list):
                item['tags'] = [normalize_field(tag) for tag in item['tags']]
            else:
                item['tags'] = normalize_field(item['tags'])

        if 'type' in item and item['type'] is not None:
            item['type'] = normalize_type(item['type'])

        if 'description' in item and item['description'] is not None:
            item['description'] = normalize_description_date_time(item['description'])

    return data

def read_data_from_file(file_path):
    """
    Reads data from a YAML file.

    Args:
        file_path (str): The path to the YAML file.

    Returns:
        dict: The data read from the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:  
        return yaml.safe_load(file)

def write_data_to_file(data, file_path):
    """
    Writes data to a YAML file.

    Args:
        data (dict): The data to be written.
        file_path (str): The path to the YAML file.
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as file:
        yaml.dump(data, file, sort_keys=False)

def process_file(file_path, spdx_licenses):
    """
    Processes a single file, normalizes it, and overwrites it.

    Args:
        file_path (str): The path to the file.
        spdx_licenses (dict): A dictionary containing license information used for normalization.
    """
    data = read_data_from_file(file_path)
    resources_data = data.get('resources', [])
    normalized_data = normalize_data(resources_data, spdx_licenses) 
    write_data_to_file({'resources': normalized_data}, file_path)
    print(f"Normalization complete. File saved as {file_path}")

def main():
    """
    Entry point of the script.
    """
    spdx_licenses = fetch_spdx_licenses()
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    resources_dir = os.path.join(base_dir, "resources")
    
    for filename in os.listdir(resources_dir):
        if filename.endswith(".yml") or filename.endswith(".yaml"):
            file_path = os.path.join(resources_dir, filename)
            process_file(file_path, spdx_licenses)

if __name__ == "__main__":
    main()
