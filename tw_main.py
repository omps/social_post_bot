"""Bot to post social media content on Instagram."""

from __future__ import print_function
import pickle
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import requests

# Modules
from bot_geocode import get_location_coordinates
from bot_hashtags import add_hashtags
from bot_images import deletePostedImage
from bot_images import saveImageToFolder
from bot_images import resizeImageForSocialMedia
from bot_sheets import buildService
from bot_sheets import getPostDetails
from bot_sheets import updateSheetsLog
from bot_telegram import notifyAdmin
from bot_twitter import authorizeTwitter
from bot_twitter import postTwitter
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
    sm_version = "tw"

    # Get a service for Google Sheets
    sheet, service = buildService()

    # Get the next available content to post on social media
    row_number, image_id, post_details = getPostDetails(sheet=sheet, sm_account=sm_version)

    sleep(1)
    #os.system("clear")

    # Save the image
    saveImageToFolder(image_id=image_id, sm_account=sm_version, post_details=post_details)
    # Resize the image
    resize_prefix = resizeImageForSocialMedia(image_id=image_id, sm_account=sm_version)

    sleep(1)

    # Post to Twitter
    api = authorizeTwitter()
    preview_link = postTwitter(api, image_prefix=resize_prefix, post_details=post_details)
    
    # Delete resized image from folder
    deletePostedImage(image_prefix=resize_prefix, image_id=image_id)

    sleep(1)

    # Update Google Sheets
    updateSheetsLog(sheet=sheet, service=service, update_image_id=image_id, sm_account=sm_version)

    # Notify administrators
    msg = f"Hello team,\nI have posted on Twitter:\n\n{preview_link}"
    notifyAdmin(admin_notify_token=telegram_token, admin_msg=msg, chat_id=chat_id)

if __name__ == ("__main__"):
    abbie() 