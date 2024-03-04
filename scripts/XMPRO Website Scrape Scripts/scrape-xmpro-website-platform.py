import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from time import sleep
import re

def scrape_page_content(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
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

def save_to_md(content, page_title, folder_path):
    try:
        # Remove special characters from the title
        title = re.sub(r'[^\w\s-]', '', page_title)

        # Ensure the title is not empty after removing special characters
        if title.strip():
            # Truncate the title if it's too long
            filename = os.path.join(folder_path, f"{title.strip()[:50]}.md")
        else:
            filename = os.path.join(folder_path, "Untitled.md")

        # Replace invalid characters in the filename
        filename = filename.replace("\n", "").replace("\xa0", " ")

        # Replace spaces with underscores in the filename
        filename = filename.replace(" ", "_")

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Content saved to {filename}")
    except Exception as e:
        print(f"Error occurred while saving to file: {e}")

def scrape_xmpro_platform_pages():
    base_url = "https://xmpro.com/platform/"
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
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
                    folder_name = "XMPro_Platform"
                    folder_path = "XMPro_Platform"
                    os.makedirs(folder_path, exist_ok=True)
                    page_title = link.text.strip()
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
                                content_md += f"{'#' * heading_level} {element.get_text().strip()}\n\n"
                            else:
                                content_md += f"{element.get_text().strip()}\n\n"
                    save_to_md(content_md, page_title, folder_path)
                else:
                    print(f"Failed to scrape the page: {page_url}")
                # Introduce a delay of 1 second before scraping the next page
                sleep(1)
        else:
            print("Could not find the sub-menu")
    except requests.RequestException as e:
        print(f"Failed to retrieve sub-menu: {e}")
    except Exception as e:
        print(f"Error occurred: {e}")

# Scrape and save pages from the "XMPro Platform" submenu
scrape_xmpro_platform_pages()
