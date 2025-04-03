# Newsletter Import Script

# 1. Import statements
import requests
from lxml import html
import os
import re
import pypdfium2 as pdfium
from generate_link_lists import read_yaml_file

# 2. Define directories and constants
newsletter_url = "https://nfdi4bioimage.de/?id=157062#c896618"
newsletter_dir = "scripts/newsletters"
output_file = os.path.join(newsletter_dir, "newsletter_links.txt")
yaml_file = "resources/nfdi4bioimage.yaml"
url_pattern = r"https?://[^\s<>\"']+"  # Regex pattern to match URLs


# 3. Main function
def main():
    """
    Retrieving links from PDF newsletters and comparing them with existing links.

    Steps:
    1. Fetch links to PDF newsletters from the website.
    2. Download the PDFs.
    3. Extract links from the downloaded PDFs.
    4. Compare extracted links with existing links in a YAML file.
    5. Save all new links to a txt file in the folder newsletters, overwriting the previous output.
    """
    print("Starting Newsletter Link Extraction Script...")

    # Step 1: Fetch PDF links from the website
    pdf_links = fetch_pdf_links(newsletter_url)
    print(f"Found {len(pdf_links)} PDF links.")

    # Step 2: Download PDFs
    download_pdfs(pdf_links, newsletter_dir)

    # Step 3: Extract links from the downloaded PDFs
    newsletter_links = extract_links_from_pdfs(newsletter_dir, url_pattern)

    # Step 4: Compare extracted links with existing YAML links
    all_links_with_status = compare_with_yaml_links(newsletter_links, yaml_file)

    # Step 5: Save all links (grouped by PDF) to a single file, overwriting the previous output
    save_links_to_file(all_links_with_status, output_file)

    print("Newsletter Link Extraction Script completed!")


def fetch_pdf_links(url):
    """
    Fetches PDF links from the given webpage URL using lxml.

    :param url: URL of the webpage to scrape.
    :return: List of PDF links found on the page.
    """
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    tree = html.fromstring(response.content)
    pdf_links = []

    for a_tag in tree.xpath("//a[@href]"):
        href = a_tag.get("href")
        if href.endswith(".pdf"):
            # Convert relative links to absolute links
            if not href.startswith("http"):
                href = requests.compat.urljoin(url, href)
            pdf_links.append(href)

    return pdf_links


def download_pdfs(pdf_links, save_dir):
    """
    Downloads PDF files from the given links and saves them to the specified directory.

    :param pdf_links: List of PDF links to download.
    :param save_dir: Directory to save the downloaded PDFs.
    """
    os.makedirs(save_dir, exist_ok=True)

    for pdf_link in pdf_links:
        pdf_name = pdf_link.split('/')[-1]  # Extract file name from the URL
        pdf_path = os.path.join(save_dir, pdf_name)

        # Download and save the PDF
        print(f"Downloading {pdf_name}...")
        response = requests.get(pdf_link)
        response.raise_for_status()

        with open(pdf_path, 'wb') as pdf_file:
            pdf_file.write(response.content)

        print(f"Saved to {pdf_path}")


def extract_links_from_pdfs(pdf_dir, url_pattern):
    """
    Extracts links from all PDFs in the given directory.

    :param pdf_dir: Directory containing PDF files to process.
    :param url_pattern: Regex pattern to extract URLs from PDF text.
    :return: Dictionary mapping PDF filenames to extracted links.
    """
    newsletter_links = {}

    for pdf_file in os.listdir(pdf_dir):
        if pdf_file.endswith(".pdf"):  # Only process PDF files
            pdf_path = os.path.join(pdf_dir, pdf_file)
            print(f"Extracting URLs from: {pdf_file}")

            try:
                pdf = pdfium.PdfDocument(pdf_path)
                pdf_links = []

                for page_number in range(len(pdf)):
                    page = pdf[page_number]
                    text = page.get_textpage().get_text_range()

                    # Find all URLs in the text using regex
                    urls = re.findall(url_pattern, text)
                    pdf_links.extend(urls)

                newsletter_links[pdf_file] = list(set(pdf_links))  # Remove duplicates

            except Exception as e:
                print(f"Error processing {pdf_file}: {e}")

    return newsletter_links


def compare_with_yaml_links(links_dict, yaml_file):
    """
    Compares extracted links with links already present in a YAML file.

    :param links_dict: Dictionary of extracted links grouped by PDF.
    :param yaml_file: Path to the YAML file containing existing links.
    :return: Dictionary with each link annotated as "new" or "existing".
    """
    existing_urls = set()

    if os.path.exists(yaml_file):
        yaml_data = read_yaml_file(yaml_file)
        for item in yaml_data.values():
            if "url" in item:
                existing_urls.add(item["url"])

    # Annotate links as "new" or "existing"
    annotated_links = {}
    for pdf, links in links_dict.items():
        annotated_links[pdf] = [(link, "new" if link not in existing_urls else "existing")
                                for link in links]

    return annotated_links


def save_links_to_file(annotated_links_dict, output_file):
    """
    Saves annotated links (grouped by PDF) to a single file.

    :param annotated_links_dict: Dictionary of links annotated as "new" or "existing".
    :param output_file: Filepath to save the links.
    """
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w") as f:
        f.write("Extracted Newsletter Links\n")
        f.write("=" * 25 + "\n\n")

        for pdf_file, links in annotated_links_dict.items():
            f.write(f"Newsletter: {pdf_file}\n")
            f.write("-" * 20 + "\n")
            for link, status in links:
                f.write(f"- {link} ({status})\n")
            f.write("\n")

    print(f"All newsletter links saved to {output_file}.")


# 5. Execute main
if __name__ == "__main__":
    main()