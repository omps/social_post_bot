"""Bot to post social media content on Instagram."""

from __future__ import print_function
import pickle
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import requests

# Modules
from bot_geocode import get_location_coordinates
from bot_images import delete_posted_image
from bot_images import save_image_to_folder
from bot_images import resize_image_for_social_media
from bot_hashtags import add_hashtags
from bot_instagram import post_instagram
from bot_telegram import notify_admin
from bot_sheets import build_service
from bot_sheets import get_post_details
from bot_sheets import update_sheets_log
from time import sleep

# Credentials for Google Sheets
from my_secrets import gspread_id
# Credentials for Telegram
from my_secrets import chat_id
from my_secrets import telegram_token

import os
import random


def abbie():
    """Main function to control A.B.B.I.E."""
    os.system("clear")
    print("Welcome to A.B.B.I.E.")
    sleep(1)

    # Set the version
    sm_version = "ig"

    # Get a service for Google Sheets
    sheet, service = build_service()

    # Get the next available content to post on social media
    row_number, image_id, post_details = get_post_details(sheet=sheet, sm_account=sm_version)

    sleep(1)
    #os.system("clear")

    # Save the image
    save_image_to_folder(image_id=image_id, sm_account=sm_version, post_details=post_details)
    # Resize the image
    resize_prefix = resize_image_for_social_media(image_id=image_id, sm_account=sm_version)

    sleep(1)

    # Post to Instagram
    preview_link = post_instagram(image_prefix=resize_prefix, post_details=post_details)

    # Delete resized image from folder
    delete_posted_image(image_prefix=resize_prefix, image_id=image_id)

    sleep(1)

    # Update Google Sheets
    update_sheets_log(sheet=sheet, service=service, update_image_id=image_id, sm_account=sm_version)

    # Notify administrators
    msg = f"Hello team,\nI have posted on Instagram:\n\n{preview_link}"
    notify_admin(admin_notify_token=telegram_token, admin_msg=msg, chat_id=chat_id)

if __name__ == ("__main__"):
    abbie() 