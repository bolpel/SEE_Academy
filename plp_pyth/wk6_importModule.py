'''
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter the image URL: https://example.com/ubuntu-wallpaper.jpg
✓ Successfully fetched: ubuntu-wallpaper.jpg
✓ Image saved to Fetched_Images/ubuntu-wallpaper.jpg

Connection strengthened. Community enriched.
'''

import requests
import os
import hashlib
from urllib.parse import urlparse

# Configuration
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
ALLOWED_CONTENT_TYPES = {'image/jpeg', 'image/png', 'image/gif', 'image/bmp', 'image/webp'}
DOWNLOAD_DIR = "Fetched_Images"

def get_filename_from_url(url):
    """Extract filename from URL or generate a default one."""
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename:
        # Generate a filename based on the URL's netloc and a hash of the URL
        url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
        filename = f"{parsed_url.netloc}_{url_hash}.jpg"
    return filename

def is_duplicate_image(content, download_dir):
    """Check if image content already exists in directory using MD5 hash."""
    content_hash = hashlib.md5(content).hexdigest()
    for existing_file in os.listdir(download_dir):
        with open(os.path.join(download_dir, existing_file), 'rb') as f:
            if hashlib.md5(f.read()).hexdigest() == content_hash:
                return True
    return False

def validate_headers(headers):
    """Validate HTTP headers before downloading content."""
    # Check Content-Type
    content_type = headers.get('Content-Type', '').split(';')[0]
    if content_type not in ALLOWED_CONTENT_TYPES:
        raise ValueError(f"Unsupported content type: {content_type}")

    # Check Content-Length
    content_length = headers.get('Content-Length')
    if content_length and int(content_length) > MAX_FILE_SIZE:
        raise ValueError(f"File size too large: {content_length} bytes")

def download_image(url, download_dir):
    """Download and save an image from a given URL."""
    try:
        # Send HEAD request first to check headers
        head_response = requests.head(url, timeout=10, allow_redirects=True)
        head_response.raise_for_status()
        validate_headers(head_response.headers)

        # Proceed with GET request if headers are valid
        response = requests.get(url, timeout=10, stream=True)
        response.raise_for_status()

        # Read content in chunks to avoid large memory usage
        content = b''
        for chunk in response.iter_content(chunk_size=8192):
            content += chunk
            if len(content) > MAX_FILE_SIZE:
                raise ValueError("File size exceeds limit during download")

        # Check for duplicates
        if is_duplicate_image(content, download_dir):
            print(f"✗ Skipped duplicate image from: {url}")
            return

        # Save the image
        filename = get_filename_from_url(url)
        filepath = os.path.join(download_dir, filename)
        
        with open(filepath, 'wb') as f:
            f.write(content)
        
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Network error for {url}: {e}")
    except Exception as e:
        print(f"✗ Error processing {url}: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Get multiple URLs from user
    urls_input = input("Please enter image URLs (separated by spaces or commas): ")
    urls = [url.strip() for url in urls_input.replace(',', ' ').split() if url.strip()]
    
    if not urls:
        print("No valid URLs provided.")
        return

    # Create directory if it doesn't exist
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    
    # Download each image
    for url in urls:
        download_image(url, DOWNLOAD_DIR)
    
    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
