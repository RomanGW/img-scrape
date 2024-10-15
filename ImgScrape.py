# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 19:32:53 2024

@author: roman
"""

# import libraries
from datetime import datetime
from bs4 import BeautifulSoup
from PIL import Image
from urllib.parse import urlparse
import os
import requests

def generate_path():
    now = datetime.now().strftime("%h-%d-%y_%H-%M-%S")
    path = f"dump/{now}"
    os.makedirs(path, exist_ok = True)
    return path

def generate_dump_log(url : str, path : str, e : Exception):
    with open(f"{path}/dump_log.txt", "a") as file:
        file.write(f"{e}")
        file.write("\nPlease send this to me at https://github.com/RomanGW !")
    
def fetch_image(link : str, path : str, i : int):
    # Open image and save
    img_data = requests.get(link, stream = True, allow_redirects = True, timeout = 10)
    
    with Image.open(img_data.raw) as image:
        image.save(f"{path}/{i}.png")

def fetch_images_from_page(url : str, page : str, path : str):
    # List of valid image extensions
    exts = (".jpg", ".png", ".gif", ".bmp")
    
    # Find all images on page
    imgs = page.find_all(["img", "images"])
    
    for i, img in enumerate(imgs):
        img_src = img.get("src")
        # Check if the image has a valid source
        if img_src and img_src.lower().endswith(exts):
            try:
                link = img_src
                if not img_src.startswith('http'):
                    link = f"https://{img_src.lstrip('//')}"
                    
                # Pull and save image.
                fetch_image(link, path, i)
                
                # Store alt_text from image into alt_img dump notepad file.
                alt_text = img.get("alt", "")
                if alt_text:
                    with open(f"{path}/img_alt.txt", "a") as file:
                        file.write(f"{i}: {alt_text}\n")
                    file.close()
            except Exception as e:
                try:
                    # If the page is invalid, attempt to pull from a page created by the img_src added onto the url link.
                    # First, get components of url by using urlparse, then construct the url using the scheme and netloc.
                    # Finally, reattempt get_page to pull images.
                    parsed_url = urlparse(url)
                    link = f"{parsed_url.scheme}://{parsed_url.netloc}"
                    fetch_image(link + img_src, path, i)
                except:
                    print(f"Failed to download {img_src}. Error: {e}")

def main():
    while True:
        url = input("Please enter the website (with header and domain) that you want to pull images from: ")
        path = generate_path()
        
        print(f"Attempting to pull images from {url}...")
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            fetch_images_from_page(url, soup, path)
            print(f"Pull requests from {url} successful. Please check {path} to ensure everything is there!")
        except Exception as e:
            # Create dump log.
            generate_dump_log(url, path, e)
            
            # Print debug text.
            print(f"Error fetching {url}. Error: {e}. \nPlease check dump_log.txt in {path} for details.")

if __name__ == "__main__":
    main()    

    