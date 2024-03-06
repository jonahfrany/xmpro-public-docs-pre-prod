import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from time import sleep
import re
import json

def scrape_page_content(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        with requests.Session() as session:
            response = session.get(url, headers=headers)
            response.raise_for_status()  # Raise an exception for bad status codes
            soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all content within the div with id="content" and class="content-area"
        content_div = soup.find('div', id='content', class_='content-area')
        if content_div:
            return content_div
        else:
            print(f"Content not found in {url}")
            return None
    except requests.RequestException as e:
        print(f"Failed to retrieve content from {url}: {e}")
        return None
    except Exception as e:
        print(f"Error occurred while fetching content from {url}: {e}")
        return None

def add_unique_title(title, titles_trunc, MAX_CHARS):
    # Truncate title to leave space for suffix if needed
    if len(title) > MAX_CHARS:
        truncated_title = title[:MAX_CHARS-3] + "..."
        if truncated_title in titles_trunc:
            # Append a number to make it unique
            i = 2
            while f"{truncated_title} ({i})" in titles_trunc:
                i += 1
            truncated_title = f"{truncated_title} ({i})"
        titles_trunc.append(truncated_title)
        return truncated_title
    else:
        if title in titles_trunc:
            # Append a number to make it unique
            i = 2
            while f"{title} ({i})" in titles_trunc:
                i += 1
            title = f"{title} ({i})"
        titles_trunc.append(title)
        return title

def save_to_md(content, page_title, page_url, folder_path):
    try:
        titles_trunc = []
        # Remove special characters from the title
        title = re.sub(r'[^\w\s-]', '', page_title)

        # Ensure the title is not empty after removing special characters
        if title.strip():
            # Truncate the title if it's too long
            truncated_title = add_unique_title(title.strip(), titles_trunc, MAX_CHARS=20)
            filename = os.path.join(folder_path, f"{truncated_title}.md")
        else:
            filename = os.path.join(folder_path, "Untitled.md")

        # Replace invalid characters in the filename
        filename = filename.replace("\n", "").replace("\xa0", " ")

        # Create the directory if it doesn't exist
        os.makedirs(folder_path, exist_ok=True)

        with open(filename, 'w', encoding='utf-8') as file:
            # Write the title
            file.write(f"# {truncated_title}\n\n")
            # Write the URL
            file.write(f"URL: {page_url}\n\n")
            # Write the content
            file.write(content)
        print(f"Content saved to {filename}")
    except Exception as e:
        print(f"Error occurred while saving to file: {e}")

def scrape_xmpro_platform_pages(folder_path):
    base_url = "https://xmpro.com/platform/"
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        with requests.Session() as session:
            response = session.get(base_url, headers=headers)
            response.raise_for_status()  # Raise an exception for bad status codes
            soup = BeautifulSoup(response.text, 'html.parser')

        # Find the sub-menu with page URLs
        sub_menu = soup.find('div', class_='sub-menu nav-dropdown')
        if sub_menu:
            # Find all links in the sub-menu
            links = sub_menu.find_all('a', href=True)
            for link in links:
                page_url = urljoin(base_url, link['href'])
                content_div = scrape_page_content(page_url)
                if content_div:
                    page_title = link.text.strip()
                    if not page_title:
                        h1_heading = content_div.find('h1')
                        if h1_heading:
                            page_title = h1_heading.get_text(strip=True)
                        else:
                            page_title = "Untitled"
                    content_md = ""
                    for element in content_div.find_all(["p", "h1", "h2", "h3", "h4", "img"]):
                        if element.name == "img":
                            prop = "src"
                            if "data-src" in element.attrs:
                                prop = "data-src"
                            w = element.get("width")
                            h = element.get("height")
                            content_md += f'<img src="{element[prop]}" width="{w}" height="{h}">\n\n'
                        else:
                            if element.name.startswith("h"):
                                heading_level = int(element.name[1])
                                content_md += f"{'#' * heading_level} {element.get_text(strip=True)}\n\n"
                            else:
                                content_md += f"{element.get_text(strip=True)}\n\n"
                    save_to_md(content_md, page_title, page_url, folder_path)
                else:
                    print(f"Failed to scrape the page: {page_url}")
                    print(f"Page URL with missing title: {page_url}")  # Print the URL with missing title
                # Introduce a delay of 1 second before scraping the next page
                sleep(1)
        else:
            print("Could not find the sub-menu")
    except requests.RequestException as e:
        print(f"Failed to retrieve sub-menu: {e}")
    except Exception as e:
        print(f"Error occurred: {e}")

# Define the path to the config file
config_file_path = 'scripts\XMPRO Website Scrape Scripts\scrape-xmpro-website-platform-config.json'

# Load JSON config file
with open(config_file_path) as json_file:
    config_data = json.load(json_file)
    folder_path = config_data.get("folderPath")

# Scrape and save pages from the "XMPro Platform" submenu
scrape_xmpro_platform_pages(folder_path)
