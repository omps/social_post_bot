"""Module to interact with PIL and handle images."""

from bot_pixabay import getImageFromPixabay
from my_secrets import post_size_guide
from PIL import Image

import os


def saveImageToFolder(image_id, sm_account, post_details):
    """Gets the image from source provider and saves to local folder."""

    # Get the image base
    image_base_word = post_details["image_link"]

    # Get the module depending on image source
    if "pixabay.com/photos/" in image_base_word:
        getImageFromPixabay(image_id=image_id, sm_account=sm_account)
    elif "istockphoto.com/photo/" in image_base_word:
        # Pass for now
        pass
    elif "pexels.com/photo" in image_base_word:
        # Pass for now
        pass


def resizeImageForSocialMedia(image_id, sm_account):
    """Resizes the original image to variations for social media."""
    # Define the size
    if sm_account == "fb":
        resize_px = post_size_guide["facebook_post"]
    elif sm_account == "ig":
        resize_px = post_size_guide["instagram_post"]
    elif sm_account == "tw":
        resize_px = post_size_guide["twitter_post"]
    elif sm_account == "pt":
        resize_px = post_size_guide["pinterest_post"]

    # Define the image prefix
    image_prefix = sm_account + "-img-original-"

    # Define the resized image prefix
    resize_prefix = "resized-" + sm_account + "-"

    print(f"Resizing picture for {sm_account.upper()} to {resize_px} pixels.")
    # Define the filepath
    image_file_path = r"/home/bot/projects/social_post_bot/images"

    # Get all files
    file_list = os.listdir(image_file_path)

    for i in file_list:
        if i.startswith(image_prefix+image_id):
            # Go to the directory
            os.chdir(image_file_path)
            print(f"Found the image")

            # Create a new filename
            new_image_filename = "resized-"+sm_account+"-"+image_id
            # Resize the image
            with Image.open(i) as new_image:
                new_image.thumbnail(resize_px)
                new_image.save(resize_prefix+image_id+".jpg", "JPEG")
                print(f"Image resized")

            # Go to the directory
            os.chdir(image_file_path)

            # Remove original image
            os.remove(i)
            print("Deleted the original image.")
            break
        
        else:
            print("Did not find the image.")

    os.chdir(r"/home/bot/projects/social_post_bot")
    print("Completed handling images.")

    return resize_prefix


def deletePostedImage(image_prefix, image_id):
    """Deletes the resized image after it has been posted."""
    # Define the filepath
    image_file_path = r"/home/bot/projects/social_post_bot/images"

    # Get all files
    file_list = os.listdir(image_file_path)
    for i in file_list:
        if i.startswith(image_prefix+image_id):
            # Go to the directory
            os.chdir(image_file_path)
            print("Found the image.")

            # Remove the resized image
            os.remove(i)
            print("Deleted the resized image.")
            break

        else:
            print("Did not find the image.")

    # Go back to directory
    os.chdir(r"/home/bot/projects/social_post_bot")