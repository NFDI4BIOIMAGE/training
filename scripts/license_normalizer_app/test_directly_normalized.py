import os
import yaml
import requests
import sys

SPDX_LICENSE_LIST_URL = "https://spdx.org/licenses/licenses.json"

# Determine the base directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.abspath(os.path.join(script_dir, "..", ".."))
UPLOAD_FOLDER = os.path.join(base_dir, "resources")
PROCESSED_FOLDER = os.path.join(base_dir, "scripts", "license_normalizer_app", "processed")

# Ensure the upload and processed directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

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

# Help the function swap the name from "Last,First" to "First Last"
def normalize_author_name(name):
    parts = [part.strip() for part in name.split(',')]
    if len(parts) == 2:
        return f"{parts[1]} {parts[0]}"
    return name

def normalize_author_list(authors):
    normalized_authors = []
    for author in authors:
        author_names = author.split(';')
        for name in author_names:
            normalized_name = normalize_author_name(name)
            normalized_authors.append(normalized_name)
    return normalized_authors

# Normalize the license names, authors, and tags in the data
def normalize_data(data, spdx_licenses):
    all_authors = set()
    all_tags = set()
    all_type = set()

    # Collect all authors and tags
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

    # Create a mapping for authors and tags
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
                # Flatten and normalize authors list
                normalized_authors = []
                for author in item['authors']:
                    normalized_authors.extend([normalize_author_name(author_mapping[a.lower().strip()]) for a in author.split(';')])
                item['authors'] = normalized_authors
            else:
                item['authors'] = [normalize_author_name(author_mapping[a.lower().strip()]) for a in item['authors'].split(';')]

        # Normalize tags
        if 'tags' in item:
            if isinstance(item['tags'], list):
                item['tags'] = [normalize_field(tag) for tag in item['tags']]
            else:
                item['tags'] = normalize_field(item['tags'])

        # Handle normalization of 'type' if present
        if 'type' in item:
            item['type'] = normalize_type(item['type'])

    return data

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def write_data_to_file(data, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as file:
        yaml.dump(data, file, sort_keys=False)

# Main function to run normalization directly
def main(input_file):
    spdx_licenses = fetch_spdx_licenses()
    data = read_data_from_file(input_file)
    resources_data = data.get('resources', [])
    normalized_data = normalize_data(resources_data, spdx_licenses)
    processed_filename = os.path.join(os.path.dirname(input_file), f"normalized_{os.path.basename(input_file)}")
    write_data_to_file({'resources': normalized_data}, processed_filename)
    print(f"Normalization complete. File saved as {processed_filename}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        main(input_file)
    else:
        from flask import Flask, request, render_template, redirect, url_for

        app = Flask(__name__)
        app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
        app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

        @app.route('/')
        def upload_form():
            message = request.args.get('message')
            return render_template('upload.html', message=message)

        @app.route('/upload', methods=['POST'])
        def upload_file():
            if 'file' not in request.files:
                return redirect(url_for('upload_form', message="No file part"))
            file = request.files['file']
            if file.filename == '':
                return redirect(url_for('upload_form', message="No selected file"))
            if file:
                filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(filename)

                spdx_licenses = fetch_spdx_licenses()
                data = read_data_from_file(filename)
                resources_data = data.get('resources', [])
                normalized_data = normalize_data(resources_data, spdx_licenses)
                processed_filename = os.path.join(app.config['PROCESSED_FOLDER'], f"normalized_{file.filename}")
                write_data_to_file({'resources': normalized_data}, processed_filename)

                # Calculate relative path of the processed file
                relative_processed_filename = os.path.relpath(processed_filename, base_dir)
                return redirect(url_for('upload_form', message=f"File processed and saved as {relative_processed_filename}"))

        app.run(debug=True)
