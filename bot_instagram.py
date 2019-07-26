"""Module to interact with Instagram."""

from instapy_cli import client
from my_secrets import ig_password
from my_secrets import ig_username

import os

def postInstagram(image_prefix, post_details):
    """Function to post to Instagram."""
    post_image_id = post_details["image_id"]+".jpg"
    post_message = post_details["text"]
    post_lat = post_details["location_lat"]
    post_long = post_details["location_long"]

    image_file_path = r"/home/bot/projects/abbie_social_post_bot/images"
    # Get all files
    file_list = os.listdir(image_file_path)
    # Get the image to post
    for i in file_list:
        if i.startswith(image_prefix+post_image_id):
            # Go to the directory
            os.chdir(image_file_path)
            post_image = i
            break
        os.chdir(r"/home/bot/projects/abbie_social_post_bot")

    with client(ig_username, ig_password) as cli:
        ig = cli.api()
        print(ig.current_user())

        post_response = cli.upload(post_image, post_message)
        media_content = post_response["media"]
        ig_code = media_content["code"]
        preview_link = (f"https://www.instagram.com/p/{ig_code}")

    return preview_link