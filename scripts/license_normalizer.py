import requests
import json
import yaml
import os

# SPDX License List URL
SPDX_LICENSE_LIST_URL = "https://spdx.org/licenses/licenses.json"

def fetch_spdx_licenses():
    """
    Fetch the SPDX license list from the SPDX website.
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
    Normalize a license name using the SPDX license list.
    """
    license_name_lower = license_name.lower().strip().replace(" ", "-")
    return spdx_licenses.get(license_name_lower, license_name_lower)

def normalize_licenses_in_data(data, spdx_licenses):
    """
    Normalize the license names in the data.
    """
    for item in data:
        if 'license' in item:
            if isinstance(item['license'], list):
                item['license'] = [normalize_license(license, spdx_licenses) for license in item['license']]
            else:
                item['license'] = normalize_license(item['license'], spdx_licenses)
    return data



def read_data_from_file(file_path):
    """
    Read YAML data from a file.
    """
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def write_data_to_file(data, file_path):
    """
    Write YAML data to a file.
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as file:
        yaml.dump(data, file, sort_keys=False)

def main():
    input_path = "C:/NFDI4BIOIMAGE/training-clean/resources/materials.yml"
    output_path = "C:/NFDI4BIOIMAGE/training-clean/scripts/normalized_materials.yml"

    # Fetch SPDX licenses
    spdx_licenses = fetch_spdx_licenses()

    # Read data from file
    data = read_data_from_file(input_path)
    resources_data = data.get('resources', [])  # Ensures it defaults to an empty list if 'resources' is not found

    # Normalize licenses in data
    normalized_data = normalize_licenses_in_data(resources_data, spdx_licenses)

    # Write normalized data to file
    write_data_to_file({'resources': normalized_data}, output_path)

    print("Data normalization complete and output saved to:", output_path)

if __name__ == "__main__":
    main()
