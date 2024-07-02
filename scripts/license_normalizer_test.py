import requests
import json

# SPDX License List URL
SPDX_LICENSE_LIST_URL = "https://spdx.org/licenses/licenses.json"

def fetch_spdx_licenses():
    """
    Fetch the SPDX license list from the SPDX website.
    """
    response = requests.get(SPDX_LICENSE_LIST_URL)
    if response.status_code == 200:
        spdx_data = response.json()
        spdx_licenses = {license["licenseId"].lower().replace(" ", "-"): license["licenseId"].lower().replace(" ", "-") for license in spdx_data["licenses"]}
        spdx_licenses.update({license["name"].lower().replace(" ", "-"): license["licenseId"].lower().replace(" ", "-") for license in spdx_data["licenses"]})
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
        if isinstance(item['license'], list):
            item['license'] = [normalize_license(license, spdx_licenses) for license in item['license']]
        else:
            item['license'] = normalize_license(item['license'], spdx_licenses)
    return data

def main():
    # Sample data
    data = [
        {
            "license": "cc-by-4.0",
            "name": "OME Documentation",
            "tags": ["omero"],
            "type": "documentation",
            "url": "https://www.openmicroscopy.org/docs/"
        },
        {
            "license": "Creative Commons Attribution 4.0 International",
            "name": "Euro-BioImaging Guide to FAIR BioImage Data - Practical Tasks",
            "description": "Hands-on exercises on FAIR Bioimage Data from the interactive online workshop Euro-BioImaging Guide to FAIR BioImage Data 2024",
            "tags": ["bioimage analysis", "FAIR-principles", "research data management"],
            "type": ["slides", "tutorial"],
            "url": "https://zenodo.org/records/11474407"
        },
        {
            "license": ["CC BY 4.0", "BSD 3-clause"],
            "name": "BioImage Analysis Notebooks",
            "tags": ["python", "bioimage analysis"],
            "type": ["book", "notebook"],
            "url": "https://haesleinhuepf.github.io/BioImageAnalysisNotebooks/intro.html"
        }
    ]

    # Fetch SPDX licenses
    spdx_licenses = fetch_spdx_licenses()

    # Normalize licenses in data
    normalized_data = normalize_licenses_in_data(data, spdx_licenses)

    # Print normalized data
    print(json.dumps(normalized_data, indent=2))

if __name__ == "__main__":
    main()
