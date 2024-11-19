# highlights download statistics
# # import statements
import os
import pandas as pd
from datetime import datetime
import requests
from pdf2image import convert_from_bytes
from io import BytesIO
from PIL import Image

folder = 'download_statistics/'
path_to_png = "docs/highlights/"

def main(): 
    """
    This script will:
    1. Load the two most recent CSV files from the 'download_statistics' folder.
    2. Compare the download counts between the two weeks.
    3. Identify the top three records with the highest download difference.
    4. Download the most downloaded files from Zenodo if they are licensed CC-BY 4.0 and save the first page as PNG.
    5. Update the README.md file with the top three downloaded records and their PNG if licensed CC-BY 4.0.
    This is done in the github CI before the website is regenerated, after every modification on the main branch.
    """

    latest_file, previous_file = get_latest_two_csv_files(folder)

    # Load the CSV data
    current_week_data = pd.read_csv(os.path.join(folder, latest_file))
    previous_week_data = pd.read_csv(os.path.join(folder, previous_file))

    # Merge data on the 'url' column to compare downloads
    merged_data = pd.merge(current_week_data, previous_week_data, on='url', suffixes=('_current', '_previous'))

    # Calculate the download difference
    merged_data['download_difference'] = merged_data['downloads_current'] - merged_data['downloads_previous']

    # Find the top three records with the highest download difference
    top_three_records = merged_data.nlargest(3, 'download_difference')

    # Print the results
    print("Top three downloaded records in the last week:")
    print(top_three_records[['url', 'download_difference']])

    # Update README.md with the top three most downloaded records
    update_readme(folder, top_three_records)

# functions
def extract_date_from_filename(filename):
    """
    Extract the date from a CSV file name. The date is expected to be in the format YYYYMMDD.
    """
    basename = os.path.basename(filename)
    date_str = basename.split('.')[0]  # Remove the .csv part
    return datetime.strptime(date_str, '%Y%m%d')

def get_latest_two_csv_files(folder):
    """
    Get the two most recent CSV files in the specified folder. 
    """
    # Get all CSV files in the folder
    csv_files = [f for f in os.listdir(folder) if f.endswith('.csv')]

    # Sort files by date (newest first)
    csv_files = sorted(csv_files, key=lambda f: extract_date_from_filename(f), reverse=True)

    # Return the two most recent files
    return csv_files[0], csv_files[1]

def download_first_pdf_file_from_zenodo(folder, record_id):
    """
    If the license is CC-BY 4.0, download the first file from a Zenodo record and save the first page as PNG. This does only work if it is a PPTX or PDF file.
    """
    # Fetch record metadata
    url = f"https://zenodo.org/api/records/{record_id}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    # Check if license is CC-BY-4.0
    license_info = data.get('metadata', {}).get('license', {}).get('id', '')
    print(f"License info from Zenodo: '{license_info}'")
    if license_info.lower() != "cc-by-4.0":
        print("Download not allowed: License is not CC-BY 4.0.")
        return
    
    # Get the first PDF file's download link and file name
    for file_info in data['files']:
        if file_info['key'].endswith('pdf'):
            file_url = file_info['links']['self']
            file_name = file_info['key']

            # Download the file content
            response = requests.get(file_url)
            response.raise_for_status()
            file_content = BytesIO(response.content)

            # Check file extension and convert based on that
            file_extension = os.path.splitext(file_name)[1].lower()
            date = datetime.now().strftime("%Y%m%d")

            os.makedirs(path_to_png, exist_ok=True)

            if file_extension == '.pdf':
                # Convert first page of PDF to PNG
                pages = convert_from_bytes(file_content.getvalue())
                img = pages[0]
                img = resize_image(img, height=300)
                img.save(path_to_png + f'{date}_first_page_{record_id}.png', 'PNG')
                print("First page of PDF saved as PNG.")
                break

            else:
                print(f"Unsupported file type: {file_extension}")

    return license_info

def resize_image(image, height):
    """
    Resize the image to the specified height while maintaining aspect ratio.

    Parameters
    ----------
    image : PIL.Image.Image
        The image to resize.
    height : int
        The desired height in pixels.
    
    Returns
    -------
    PIL.Image.Image
        The resized image.
    """
    aspect_ratio = image.width / image.height
    new_width = int(aspect_ratio * height)
    return image.resize((new_width, height), Image.LANCZOS)

# Define the format of your PNG file
def get_latest_png_filename(id):
    """
    Get the filename of the latest PNG file. The file name is expected to be in the format YYYYMMDD_first_page.png.
    """
    date_str = datetime.now().strftime("%Y%m%d")
    return path_to_png + f"{date_str}_first_page_{id}.png"

# Function to update README.md
def update_readme(folder, top_records):
    """
    Update the README.md file with the top three downloaded records.
    """
    readme_path = "docs/readme.md"
    
    highlights = []
    count = 0
    for _, record in top_records.iterrows():
        record_id = record['url'].split('/')[-1]
        license_info = download_first_pdf_file_from_zenodo(folder, record_id)
        title = get_title_of_zenodo_record(record['url'])

        count = count + 1
        record_highlight = f"""\n{count}. [{title}]({record['url']}) by {record['authors_current']} ({record['download_difference']} downloads), licensed [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)"""

        print("license_info", license_info)
        if license_info == "cc-by-4.0":
            latest_png = get_latest_png_filename(record_id)
            print("latest_png", latest_png, os.path.isfile(latest_png))
            if os.path.isfile(latest_png):
                record_highlight += f"\n\n![latest PNG]({latest_png.replace('docs/', '')})"
        
        highlights.append(record_highlight)
    
    highlight_text = "\n".join(highlights)

    # Read and update README.md assuming similar logic to existing code for replacing content
    with open(readme_path, 'r') as file:
        content = file.read()

    content = content.replace("{top_three_downloads}", highlight_text)

    # Write the updated content back to the README
    with open(readme_path, 'w') as file:
        file.writelines(content)
    
    print(f"README.md updated with the latest top 3 downloads.")

def get_title_of_zenodo_record(url):
    """Determine the title of a Zenodo record based on its URL."""
    record_id = url.split('/')[-1]
    api_url = f"https://zenodo.org/api/records/{record_id}"
    response = requests.get(api_url)
    record_data = response.json()
    return record_data['metadata']['title']


# Run the script
if __name__ == "__main__":
    main()
