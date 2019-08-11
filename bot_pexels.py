"""Module to handle Pexels."""

import requests
from bs4 import BeautifulSoup as bs
import os

sm_account = 'tw'

def getImageFromPexels(image_id, sm_account):
    """Function to get image from Pexels."""
    # Define the URL
    URL = image_id
    image_identifier = image_id.split('.com/photo/')[-1]
    image_identifier = image_identifier.split('-')[-1]
    image_identifier = image_identifier.replace('/', '')
    # Move to image directory
    os.chdir('/home/bot/projects/social_post_bot/images')

    # Download page
    page = requests.get(URL)
    soup = bs(page.text, 'html.parser')

    # Find the image
    image_div = soup.find_all('div', {'class': 'photo-page__photo'})[0]
    image_a = image_div.find_all('a')[0]
    image_href = image_a['href']
    response = requests.get(image_href)
    if response.status_code == 200:
        with open(f'{sm_account}-img-original-{str(image_identifier)}.jpg', 'wb') as f:
            f.write(requests.get(image_href).content)
            f.close()

