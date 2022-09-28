# Ex 7: Simple scraber with requests
"""
1. Create an application that asks for an url.
2. Then Download that html page, and its images, icons etc. and change it so it will work locally on your computer. Locally means that you should be able to cut your internet connection and still have a functionig html page.
3. When done push all files to you github account. (you are allowed to manualy create an online repo and feed the clone url to your program. but the rest should be done through python).
You will have to use the requests module, the OS module and the subprocesses module for this taks."""

import os
from bs4 import BeautifulSoup
import urllib.request
import requests

print('enter url')
url = input()
# 'https://google.com/'
dir_path = 'D:/temp_scrubber'
file_name = 'test_html.txt'
full_save_path = os.path.join(dir_path, file_name)

if not os.path.exists(dir_path):
    os.makedirs(dir_path)

def save_html_to_file():
    urllib.request.urlretrieve(url, full_save_path)

#send get request
response = requests.get(url)

#parse response text
html_page = BeautifulSoup(response.text, 'html.parser')

def handle_images():
    # find all images in URL
    images = html_page.find_all("img")


    for index, image in enumerate(images):
        image_url = 'HTTPS:' + image.get("src")      #img src value
        print(images)
        image_extension = image_url.split(".")[-1]       #get image extension

        #get image data
        image_bytes = requests.get(image_url).content
        
        if image_bytes:
        
            #write the image data
            with open(dir_path + f"/Image_{index+1}.{image_extension}", "wb") as file:
                file.write(image_bytes)    

save_html_to_file()

handle_images()