import os
import re
import yaml
import requests
import pandas as pd
import spacy
import numpy as np
from nameparser import HumanName

# Initialize spaCy NLP pipeline
nlp = spacy.load('en_core_web_sm')

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

    Returns
    -------
    dict
        A dictionary with license names as keys and their IDs as values.
    """
    response = requests.get(SPDX_LICENSE_LIST_URL)
    if response.status_code == 200:
        spdx_data = response.json()
        spdx_licenses = {
            license["licenseId"].lower().replace(" ", "-"): license["licenseId"]
            for license in spdx_data["licenses"]
        }
        spdx_licenses.update({
            license["name"].lower().replace(" ", "-"): license["licenseId"]
            for license in spdx_data["licenses"]
        })
        return spdx_licenses
    else:
        raise Exception("Failed to fetch SPDX licenses")

def normalize_license(license_name, spdx_licenses):
    """
    Normalizes a license name to match SPDX identifiers.

    Parameters
    ----------
    license_name : str
        The name of the license to be normalized.
    spdx_licenses : dict
        A dictionary of available SPDX licenses.

    Returns
    -------
    str
        The normalized license name.
    """
    if license_name is None or (isinstance(license_name, float) and np.isnan(license_name)):
        return license_name  # Return as is if None or NaN

    # Ensure license_name is a string
    license_name = str(license_name)

    # Apply the normalization mapping first
    license_name = normalization_mapping.get(license_name, license_name)

    # Normalize the license name to match SPDX format
    license_name_lower = license_name.lower().strip().replace(" ", "-")

    # Get the normalized license from SPDX list or keep the original
    normalized_license = spdx_licenses.get(license_name_lower, license_name)

    return normalized_license

def normalize_field(field):
    """
    Normalizes a single field (e.g., tags).

    Parameters
    ----------
    field : str or list
        The field to be normalized.

    Returns
    -------
    str or list
        The normalized field.
    """
    if field is None or (isinstance(field, float) and np.isnan(field)):
        return field  # Return as is if None or NaN

    if isinstance(field, list):
        return [normalization_mapping.get(item.strip().title(), item.strip().title()) for item in field if pd.notnull(item)]
    else:
        return normalization_mapping.get(field.strip().title(), field.strip().title())

def normalize_type(type_field):
    """
    Ensures the 'type' field is a list and normalizes its contents.

    Parameters
    ----------
    type_field : str or list
        The 'type' field to be normalized.

    Returns
    -------
    list
        The normalized 'type' field.
    """
    if type_field is None or (isinstance(type_field, float) and np.isnan(type_field)):
        return type_field  # Return as is if None or NaN

    if isinstance(type_field, list):
        return [type_.strip().title() for type_ in type_field if pd.notnull(type_)]
    else:
        return [type_field.strip().title()]

def normalize_author_list(authors):
    if authors is None or (isinstance(authors, float) and np.isnan(authors)):
        return authors  # Return as is if None or NaN

    normalized_authors = []

    if isinstance(authors, list):
        authors_str = ', '.join(str(author) for author in authors)
    else:
        authors_str = str(authors)

    # Replace common delimiters with commas
    authors_str = re.sub(r'[;\n]| and ', ',', authors_str)

    # Use spaCy to parse the text
    doc = nlp(authors_str)

    # Extract PERSON entities
    person_names = [ent.text for ent in doc.ents if ent.label_ == 'PERSON']

    # If spaCy didn't find any PERSON entities, fall back to splitting
    if not person_names:
        person_names = re.split(r',\s*(?=[A-Z])', authors_str)

    for name in person_names:
        name = name.strip().strip('"').strip("'")
        if not name:
            continue

        # Handle "Lastname, Firstname(s)" format
        if ',' in name:
            parts = [part.strip() for part in name.split(',', 1)]
            if len(parts) == 2:
                last_name = parts[0]
                first_names = parts[1]
                name = f"{first_names} {last_name}"
            else:
                name = name.replace(',', '')
        # Use nameparser to normalize the name
        hn = HumanName(name)
        hn.capitalize()
        name_parts = [hn.first, hn.middle, hn.last]
        normalized_name = ' '.join(part for part in name_parts if part)
        normalized_authors.append(normalized_name)

    return normalized_authors


def normalize_description_date_time(description):
    """
    Normalizes date/time strings within the description.

    Parameters
    ----------
    description : str
        The description containing the date/time.

    Returns
    -------
    str
        The normalized description.
    """
    # Remove unwanted Unicode characters
    if description is None or (isinstance(description, float) and np.isnan(description)):
        return description  # Return as is if None or NaN

    # Remove unwanted Unicode characters
    normalized_description = re.sub(r'\xE2\u20AC\xAF', '', description)

    # Add a space between time and AM/PM if not present
    normalized_description = re.sub(r'(\d)(AM|PM)', r'\1 \2', normalized_description)

    return normalized_description

def normalize_data(data, spdx_licenses):
    df = pd.DataFrame(data)

    # Normalize licenses
    if 'license' in df.columns:
        df['license'] = df['license'].apply(
            lambda x: [normalize_license(lic, spdx_licenses) for lic in x if lic is not None] if isinstance(x, list)
            else normalize_license(x, spdx_licenses)
        )

    # Normalize authors
    if 'authors' in df.columns:
        df['authors'] = df['authors'].apply(normalize_author_list)

    # Normalize tags
    if 'tags' in df.columns:
        df['tags'] = df['tags'].apply(normalize_field)

    # Normalize type
    if 'type' in df.columns:
        df['type'] = df['type'].apply(normalize_type)

    # Normalize description
    if 'description' in df.columns:
        df['description'] = df['description'].apply(normalize_description_date_time)

    return df.to_dict(orient='records')


def read_data_from_file(file_path):
    """
    Reads data from a YAML file.

    Parameters
    ----------
    file_path : str
        The path to the YAML file.

    Returns
    -------
    dict
        The data read from the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:  
        return yaml.safe_load(file)

def write_data_to_file(data, file_path):
    """
    Writes data to a YAML file.

    Parameters
    ----------
    data : dict
        The data to be written.
    file_path : str
        The path to the YAML file.
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as file:
        yaml.dump(data, file, sort_keys=False, allow_unicode=True)

def process_file(file_path, spdx_licenses):
    """
    Processes a single file, normalizes it, and overwrites it.

    Parameters
    ----------
    file_path : str
        The path to the file.
    spdx_licenses : dict
        A dictionary containing license information used for normalization.
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
