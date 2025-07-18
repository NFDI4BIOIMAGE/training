# Checking URL availability 
import yaml
import requests
import concurrent.futures
import time
import datetime
import random
import os

# File paths
yaml_file_path = "resources/nfdi4bioimage.yml"

#get current date
date = datetime.datetime.now().strftime("%Y%m%d")

#create filename
log_file = f'scripts/url_validity_check/{date}_url_check_results.log'

# Ensure log directory exists
os.makedirs(os.path.dirname(log_file), exist_ok=True)

# Max retries for failed requests
max_retries = 3
base_backoff = 2  

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
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Mozilla/5.0 (X11; Linux x86_64)",
    ]
    
    headers = {
        "User-Agent": random.choice(user_agents),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.google.com/",
        "DNT": "1",  # Do Not Track
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Cache-Control": "no-cache"
    }

    last_error = ""
    for attempt in range(1, max_retries + 1):
        try:
            response = requests.get(url, headers=headers, timeout=15, allow_redirects=True)
            status = response.status_code

            if status == 200:
                return f"✅ {url} is reachable (Attempt {attempt})"
            elif status == 429:
                return f"⚠️ {url} is rate-limited (429), considering it reachable."
            elif status in (404, 410):
                return f"❌ {url} returned {status} (Attempt {attempt})"
            elif status in (403, 400):
                return f"⚠️ {url} returned status {status}. It may be blocking bots. (Attempt {attempt})"
            else:
                last_error = f"{url} returned status {status} (Attempt {attempt}), final URL: {response.url}"

        except requests.exceptions.RequestException as e:
            last_error = f"{url} failed: {repr(e)}"

        sleep_time = base_backoff ** attempt + random.uniform(0, 1)
        time.sleep(sleep_time)

    return f"⚠️ {url} is potentially reachable but failed after {max_retries} attempts. Last error: {last_error}"

def log_results(results):
    """Log results to a file."""
    with open(log_file, "w") as file:
        for result in results:
            file.write(result + "\n")

if __name__ == "__main__":
    main()