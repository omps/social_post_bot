"""Module to interact with Pixabay."""

from my_secrets import pixabay_api_key as API_KEY

import json
import os
import re
import requests


def get_image_from_pixabay(image_id, sm_account):
    """Function to get image from Pixabay."""
    # Define the base url
    URL = f"https://pixabay.com/api/?key={API_KEY}&id={image_id}"
    # Move to directory
    os.chdir("/home/bot/projects/abbie_social_post_bot/images")

    def get_pixabay_url(url, image_id):
        """Function to get the formatted url."""
        response = requests.get(url)
        content = response.content.decode("utf8")
        js = json.loads(content)
        print("Completed Pixabay API call.")
        return js

    def get_pixabay_large_image(js, image_id):
        """Function to get the image from the url."""
        # Get the hit
        hit = js.get("hits")[0]
        hit_id = hit["id"]
        # Make sure you have the correct image
        if str(hit_id) == (image_id):
            hit_link = hit["largeImageURL"]
            print(f"Found image {hit_id} with URL {hit_link}")

        return hit_id, hit_link

    def save_image(hit_id, hit_link):
        """Get the image from the url."""
        image = requests.get(hit_link)
        #  Print the status code
        if image.status_code == 200:
            print(f"Status code {str(image.status_code)}")
            # Get the content
            with open(f"{sm_account}-img-original-{str(hit_id)}.jpg", "wb") as f:
                f.write(requests.get(hit_link).content)
                f.close()
            os.chdir("..")
            print("Image saved.")
            

    # Get the json from the API
    js = get_pixabay_url(url=URL, image_id=image_id)
    # Get the image details
    hit_id, hit_link = get_pixabay_large_image(js=js, image_id=image_id)
    # Get the image
    image_content = save_image(hit_id=hit_id, hit_link=hit_link)