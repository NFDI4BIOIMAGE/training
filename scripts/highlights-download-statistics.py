# highlights download statistics
# # import statements
import os
import pandas as pd
from datetime import datetime
import requests
import pypdfium2
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

    try:
        latest_file, previous_file = get_latest_two_csv_files(folder)
    except FileNotFoundError as e:
        print(f"No valid CSV files found: {e}")
        return

    # Load the CSV data with defensive handling
    try:
        current_week_data = pd.read_csv(os.path.join(folder, latest_file))
    except pd.errors.EmptyDataError:
        print(f"Latest CSV '{latest_file}' is empty or has no columns. Aborting.")
        return
    except Exception as e:
        print(f"Failed to read latest CSV '{latest_file}': {e}")
        return

    try:
        previous_week_data = pd.read_csv(os.path.join(folder, previous_file))
    except pd.errors.EmptyDataError:
        print(f"Previous CSV '{previous_file}' is empty or has no columns. Aborting.")
        return
    except Exception as e:
        print(f"Failed to read previous CSV '{previous_file}': {e}")
        return

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
    csv_candidates = [f for f in os.listdir(folder) if f.endswith('.csv')]

    # Parse dates from filenames and ignore files that don't match the expected format
    dated_files = []
    for f in csv_candidates:
        try:
            dt = extract_date_from_filename(f)
            dated_files.append((f, dt))
        except Exception:
            continue

    # Sort files by date (newest first)
    dated_files.sort(key=lambda t: t[1], reverse=True)

    # Collect two valid CSV files (non-empty and parseable)
    valid_files = []
    for fname, _ in dated_files:
        fullpath = os.path.join(folder, fname)
        try:
            if os.path.getsize(fullpath) == 0:
                continue
        except OSError:
            continue

        # Quick parse test: try to read one row to ensure there are columns
        try:
            pd.read_csv(fullpath, nrows=1)
        except Exception:
            continue

        valid_files.append(fname)
        if len(valid_files) >= 2:
            break

    if len(valid_files) < 2:
        raise FileNotFoundError(f"Could not find two valid CSV files in '{folder}'. Found: {valid_files}")

    return valid_files[0], valid_files[1]

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
        if file_info['key'].endswith('.pdf'):
            file_url = file_info['links']['self']

            # Download the file content into memory
            try:
                response = requests.get(file_url)
                response.raise_for_status()
                file_content = BytesIO(response.content)
            except:
                continue

            # Convert first page of PDF to PNG using pdfium
            pdf = pypdfium2.PdfDocument(file_content)
            page = pdf[0]
            pil_image = page.render(
                scale=2,  
                rotation=0
            ).to_pil()

            # Save the image
            date = datetime.now().strftime("%Y%m%d")
            os.makedirs(folder, exist_ok=True)
            png_path = os.path.join(folder, f'{date}_first_page_{record_id}.png')
            pil_image.save(png_path, 'PNG')
            print(f"First page of PDF saved as PNG at {png_path}.")
            break

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
    # Determine resampling method safely to avoid static type-checker attribute errors
    resample_method = None
    # Prefer the Resampling enum when available (Pillow >= 9.1)
    resampling_enum = getattr(Image, "Resampling", None)
    if resampling_enum is not None:
        resample_method = getattr(resampling_enum, "LANCZOS", None)
    # Fallback to legacy attribute via getattr to avoid Pylance attribute warnings
    if resample_method is None:
        resample_method = getattr(Image, "LANCZOS", getattr(Image, "BICUBIC", None))
    return image.resize((new_width, height), resample_method)

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
