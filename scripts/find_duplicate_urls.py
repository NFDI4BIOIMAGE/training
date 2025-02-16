import yaml
from collections import Counter
from pathlib import Path

def find_duplicate_urls(filename):
    """
    Navigate recursively through the given YAML file to find and print duplicate URLs.

    Parameters
    ----------
    filename : str or Path
        Path to the YAML file to analyze.

    Returns
    -------
    None
    """
    def extract_urls(data):
        """
        Recursively extract all URLs from a nested data structure.

        Parameters
        ----------
        data : dict, list, or other
            The data structure to traverse.

        Returns
        -------
        list of str
            List of URLs found in the structure.
        """
        urls = []
        if isinstance(data, dict):
            for key, value in data.items():
                if key == "url":
                    if isinstance(value, list):
                        urls.extend(value)
                    elif isinstance(value, str):
                        urls.append(value)
                else:
                    urls.extend(extract_urls(value))
        elif isinstance(data, list):
            for item in data:
                urls.extend(extract_urls(item))
        return urls

    with open(filename, 'r') as file:
        data = yaml.safe_load(file)

    urls = extract_urls(data)
    duplicates = [url for url, count in Counter(urls).items() if count > 1]

    for duplicate in duplicates:
        print(duplicate)

if __name__ == "__main__":
    yml_file = Path("resources/nfdi4bioimage.yml")
    find_duplicate_urls(yml_file)
