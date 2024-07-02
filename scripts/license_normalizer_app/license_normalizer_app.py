from flask import Flask, request, render_template, redirect, url_for
import os
import yaml
import requests

app = Flask(__name__)
UPLOAD_FOLDER = 'C:/NFDI4BIOIMAGE/training-clean/resources'
PROCESSED_FOLDER = 'C:/NFDI4BIOIMAGE/training-clean/scripts/license_normalizer_app/processed'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

# Ensure the upload and processed directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

SPDX_LICENSE_LIST_URL = "https://spdx.org/licenses/licenses.json"

def fetch_spdx_licenses():
    response = requests.get(SPDX_LICENSE_LIST_URL)
    if response.status_code == 200:
        spdx_data = response.json()
        spdx_licenses = {license["licenseId"].lower().replace(" ", "-"): license["licenseId"] for license in spdx_data["licenses"]}
        spdx_licenses.update({license["name"].lower().replace(" ", "-"): license["licenseId"] for license in spdx_data["licenses"]})
        return spdx_licenses
    else:
        raise Exception("Failed to fetch SPDX licenses")

def normalize_license(license_name, spdx_licenses):
    license_name_lower = license_name.lower().strip().replace(" ", "-")
    return spdx_licenses.get(license_name_lower, license_name_lower)

def normalize_licenses_in_data(data, spdx_licenses):
    for item in data:
        if 'license' in item:
            if isinstance(item['license'], list):
                item['license'] = [normalize_license(license, spdx_licenses) for license in item['license']]
            else:
                item['license'] = normalize_license(item['license'], spdx_licenses)
    return data

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def write_data_to_file(data, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as file:
        yaml.dump(data, file, sort_keys=False)

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        spdx_licenses = fetch_spdx_licenses()
        data = read_data_from_file(filename)
        resources_data = data.get('resources', [])
        normalized_data = normalize_licenses_in_data(resources_data, spdx_licenses)
        processed_filename = os.path.join(app.config['PROCESSED_FOLDER'], f"normalized_{file.filename}")
        write_data_to_file({'resources': normalized_data}, processed_filename)

        return f"File processed and saved as {processed_filename}"

if __name__ == "__main__":
    app.run(debug=True)
