"""Module to interact with Google Sheets."""

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from bot_geocode import get_location_coordinates
from bot_hashtags import add_hashtags
from my_secrets import gspread_id
from time import sleep

# Google Sheets variables
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = gspread_id
FULL_RANGE_NAME = 'Main!A4:N'

def buildService():
    """
    Builds an API service with Google Sheets. 
    Returns a sheet connection and a service.
    """
    creds = None
    # Delete token.pickle if changing authorization/scope
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    # If no valid credentials exist, allow the user to log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '/home/bot/projects/abbie_social_post_bot/client_secret.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    print('Completed "build_service" function')
    return sheet, service


def getPostDetails(sheet, sm_account):
    """Get next available post content for social media."""
    # Get the result
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=FULL_RANGE_NAME).execute()
    values = result.get("values", [])

    # If no data found
    if not values:
        print("No data found.")

    # If data found, continue
    else:
        print("Completed Google Sheets data extraction.")
        for idx, row, in enumerate(values):
            row_number = idx+4
            image_id = row[0]
            if sm_account == "ig":
                already_posted_on_social_media = row[2]
            elif sm_account == "tw":
                already_posted_on_social_media = row[3]
            elif sm_account == "fb":
                already_posted_on_social_media = row[1]
            elif sm_account == "pt":
                already_posted_on_social_media = row[4]

            # For images that were already posted 
            if already_posted_on_social_media == "Yes":
                pass
            
            # For images that have not yet been posted
            elif already_posted_on_social_media == "No" and image_id:
                post_details = {}
                post_message = row[7]
                character_length = row[12]
                hashtags = row[9]
                location = row[8]
                image_link = row[10]

                # Get the coordinates
                location_lat, location_long = get_location_coordinates(location=location)

                # Add hashtags
                post_message = add_hashtags(post_message=post_message, hashtags=hashtags, sm_account=sm_account)
                post_details.update({"text": post_message,})
                post_details.update({"image_id": str(image_id),})
                post_details.update({"location_lat": str(location_lat),})
                post_details.update({"location_long": str(location_long),})
                post_details.update({"image_link": str(image_link),})

                print("Found content to post")
                print(f"Image ID {image_id} | Already posted on Social Media: {already_posted_on_social_media}")
                break
        print(f"Post details: {post_details}")
        return row_number, image_id, post_details


def updateSheetsLog(sheet, service, update_image_id, sm_account):
    """Update Google Sheets after content has been posted."""
    # Define the columns related to each social media account
    sheets_social_media_columns = {
        "tw": ["D", "E"],
        "ig": ["C", "D"],
        "fb": ["B", "C"],
        "pt": ["E", "F"],
    }

    # Get the result
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=FULL_RANGE_NAME).execute()
    values = result.get("values", [])

    # If no data found
    if not values:
        print("No data data found")
    # If data found
    else:
        for idx, row in enumerate(values):
            target_row = idx+4
            check_image_id = row[0]
            if str(update_image_id) == str(check_image_id):
                UPDATE_RANGE_NAME = f"Main!{sheets_social_media_columns[sm_account][0]+str(target_row)}:{sheets_social_media_columns[sm_account][1]+str(target_row)}"
                Body = {
                    "majorDimension": "ROWS",
                    "values": [
                        ["Yes"],
                    ],
                }

                # Update Google Sheets
                result = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                        range=UPDATE_RANGE_NAME, valueInputOption="RAW", body=Body).execute()
                
                print(f"Google Sheets updated")
                break