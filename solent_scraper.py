import os
import requests
from bs4 import BeautifulSoup
import pathlib
from pathlib import Path


def download_image(img_url, folder_name):
    try:
        response = requests.get(img_url)
        file_name = os.path.basename(img_url)
        file_path = os.path.join(folder_name, file_name)
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print("Image downloaded successfully:", file_path)
    except Exception as e:
        print("Error downloading image:", e)

html_text = requests.get("https://solent.co.za/gallery/spares").text
soup = BeautifulSoup(html_text, "lxml")
images = soup.find_all("img", class_="img-responsive product-image")

directory_name = pathlib.Path("Spares/Spares-Dir/")
directory_name.mkdir(parents=True, exist_ok=True)

for image in images:
    img_url = image['src']
    download_image(img_url, directory_name)
