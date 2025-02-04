# Checking URL availability 
import yaml
import requests
import concurrent.futures
import time
import datetime
import random

# File paths
yaml_file_path = "resources/nfdi4bioimage.yml"

#get current date
date = datetime.datetime.now().strftime("%Y%m%d")

#create filename
log_file = f'scripts/url_validity_check/{date}_url_check_results.log'

# Max retries for failed requests
max_retries = 3

def main():
    """
    URL Availability Checker
    """
    urls = extract_urls(yaml_file_path)

    # Run URL checks in parallel for efficiency
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(check_url, urls))

    # Print and log results
    for result in results:
        print(result)

    log_results(results)

def extract_urls(file_path):
    """Extract URLs from a YAML file and ensure they are properly formatted."""
    with open(file_path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)

    urls = []
    for entry in data.get('resources', []):
        if isinstance(entry.get('url'), list):
            urls.extend(entry['url'])  # Flatten list of URLs
        elif isinstance(entry.get('url'), str):
            urls.append(entry['url'])
    
    return urls

def check_url(url):
    """Check if a URL is reachable with retries and logging."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    for attempt in range(1, max_retries + 1):
        try:
            response = requests.get(url, headers=headers, timeout=5, allow_redirects=True)
            
            if response.status_code == 200:
                return f"✅ {url} is reachable (Attempt {attempt})"
            elif response.status_code == 429:
                return f"✅ {url} is rate-limited (429), considering it reachable."
            elif response.status_code in [403, 404]:
                return f"❌ {url} returned status {response.status_code}. It may be blocking bots. (Attempt {attempt})"
            else:
                return f"❌ {url} returned status {response.status_code} (Attempt {attempt})"
        except requests.exceptions.ConnectionError:
            return f"❌ {url} is unreachable (Connection Error) (Attempt {attempt})"
        except requests.exceptions.Timeout:
            return f"❌ {url} is unreachable (Timeout) (Attempt {attempt})"
        except requests.exceptions.RequestException as e:
            return f"❌ {url} failed due to {e} (Attempt {attempt})"
        
        # Wait before retrying
        time.sleep(random.uniform(1, 3))

    return f"❌ {url} is unreachable after {max_retries} attempts."

def log_results(results):
    """Log results to a file."""
    with open(log_file, "w") as file:
        for result in results:
            file.write(result + "\n")

if __name__ == "__main__":
    main()