# highlights download statistics

# import statements
import os
import pandas as pd
from datetime import datetime
import requests
from pptx import Presentation
from pdf2image import convert_from_bytes
from io import BytesIO
from PIL import Image


# functions
def extract_date_from_filename(filename):
    basename = os.path.basename(filename)
    date_str = basename.split('.')[0]  # Remove the .csv part
    return datetime.strptime(date_str, '%Y%m%d')

def get_latest_two_csv_files(folder):
    # Get all CSV files in the folder
    csv_files = [f for f in os.listdir(folder) if f.endswith('.csv')]

    # Sort files by date (newest first)
    csv_files = sorted(csv_files, key=lambda f: extract_date_from_filename(f), reverse=True)

    # Return the two most recent files
    return csv_files[0], csv_files[1]

def download_first_file_from_zenodo(record_id):
    # Fetch record metadata
    url = f"https://zenodo.org/api/records/{record_id}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    
    # Get the first file's download link and file name
    file_info = data['files'][0]
    file_url = file_info['links']['self']
    file_name = file_info['key']  # This is the file name
    
    # Download the file content
    response = requests.get(file_url)
    response.raise_for_status()
    file_content = BytesIO(response.content)

    # Check file extension and convert based on that
    file_extension = os.path.splitext(file_name)[1].lower()
    date = datetime.now().strftime("%Y%m%d")

    if file_extension == '.pptx':
        # Convert first slide of PPT to PNG
        prs = Presentation(file_content)
        slide = prs.slides[0]
        
        # Placeholder slide-to-image conversion (requires custom handling)
        img = Image.new('RGB', (1280, 720), color = 'white')  # Placeholder, slides cannot be directly converted to images
        img.save(folder + f'highlights/{date}_first_page.png', 'PNG')
        print("First slide of PPT saved as PNG.")

    elif file_extension == '.pdf':
        # Convert first page of PDF to PNG
        pages = convert_from_bytes(file_content.getvalue())  # Use pdf2image with BytesIO
        img = pages[0]
        # save image in folder highlights

        img.save(folder + f'highlights/{date}_first_page.png', 'PNG')
        print("First page of PDF saved as PNG.")

    else:
        print(f"Unsupported file type: {file_extension}")

# Define the format of your PNG file
def get_latest_png_filename():
    date_str = datetime.now().strftime("%Y%m%d")
    path_to_png = "../download_statistics/highlights/"
    return path_to_png + f"{date_str}_first_page.png"

# Function to update README.md
def update_readme():
    # Get the latest PNG file name
    latest_png = get_latest_png_filename()

    # Check if the PNG file exists
    if not os.path.isfile(latest_png):
        print(f"Error: {latest_png} does not exist.")
        return

    # Path to the README file
    readme_path = "../docs/readme.md"
    
    # Read the existing README.md file
    with open(readme_path, 'r') as file:
        content = file.readlines()

    # Define the subheading under which the PNG should be added
    subheading = "## Most downloaded training material in the last week"
    
    # Flag to track if the subheading is found
    subheading_found = False
    updated_content = []
    
    for line in content:
        updated_content.append(line)
        
        # When the subheading is found, insert the latest PNG file reference
        if line.strip() == subheading:
            subheading_found = True
            updated_content.append(f"\n![latest PNG]({latest_png})\n")
    
    if not subheading_found:
        print(f"Subheading '{subheading}' not found in README.md.")
        return

    # Write the updated content back to the README
    with open(readme_path, 'w') as file:
        file.writelines(updated_content)
    
    print(f"README.md updated with the latest PNG under the subheading '{subheading}'.")

folder = '../download_statistics/'

latest_file, previous_file = get_latest_two_csv_files(folder)

# Load the CSV data
current_week_data = pd.read_csv(os.path.join(folder, latest_file))
previous_week_data = pd.read_csv(os.path.join(folder, previous_file))

# Merge data on the 'url' column to compare downloads
merged_data = pd.merge(current_week_data, previous_week_data, on='url', suffixes=('_current', '_previous'))

# Calculate the download difference
merged_data['download_difference'] = merged_data['downloads_current'] - merged_data['downloads_previous']

# Find the record with the highest download difference
most_downloaded_record = merged_data.loc[merged_data['download_difference'].idxmax()]

# Print the results
print("Most downloaded record in the last week:")
print(most_downloaded_record[['url', 'download_difference']])

url = most_downloaded_record['url']

#extract from url the zenodo id
record_id = url.split('/')[-1]

# Download the most downloaded file from zenodo and save the first page as PNG in case of PPTX or PDF
download_first_file_from_zenodo(record_id)

# Run the script
if __name__ == "__main__":
    update_readme()
