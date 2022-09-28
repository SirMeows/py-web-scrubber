# Ex 7: Simple scraber with requests

# 1. Create an application that asks for an url.
# 2. Then Download that html page, and its images, icons etc.

import os
from bs4 import BeautifulSoup
import urllib.request
import requests

print('enter url')
url = input()
# example url 'https://google.com/'
dir_path = 'C:/tmp/web_scrubber/'
file_name = 'test_html.txt'
full_save_path = os.path.join(dir_path, file_name)

if not os.path.exists(dir_path):
    os.makedirs(dir_path)

def save_html_to_file():
    urllib.request.urlretrieve(url, full_save_path)

response = requests.get(url)

html_page = BeautifulSoup(response.text, 'html.parser')

def handle_images():

    images = html_page.find_all("img")

    for index, image in enumerate(images):
        image_url = 'HTTPS:' + image.get("src")
        image_extension = image_url.split(".")[-1]

        image_bytes = requests.get(image_url).content
        
        if image_bytes:
        
            with open(dir_path + f"/Image_{index+1}.{image_extension}", "wb") as file:
                file.write(image_bytes)    

save_html_to_file()

handle_images()

print("see downloaded files in " + dir_path + " directory ")