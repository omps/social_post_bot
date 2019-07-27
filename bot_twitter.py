"""Module to interact with Twitter via Tweepy."""

from my_secrets import consumer_key as CONSUMER_KEY
from my_secrets import consumer_secret as CONSUMER_SECRET
from my_secrets import access_token as ACCESS_TOKEN
from my_secrets import access_secret as ACCESS_SECRET

import json
import os
import tweepy


def authorizeTwitter():
    """Function to authorize a connection with Twitter."""
    # Get authorization
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)

    return api


def postTwitter(api, image_prefix, post_details):
    """Post the contents to Twitter."""
    image_file_path = r"/home/bot/projects/social_post_bot/images"
    
    # Get all files
    file_list = os.listdir(image_file_path)

    # Get the image to post
    for i in file_list:
        if i.startswith(image_prefix+post_details["image_id"]):
            # Go to the directory
            os.chdir(image_file_path)
            tweet_image = i
            break
        os.chdir(r"/home/bot/projects/social_post_bot/")

    # Get the text to post
    message = post_details["text"]
    # Get the geocode coordinates
    tw_lat = post_details["location_lat"]
    tw_long = post_details["location_long"]

    post_media_response = api.update_with_media(tweet_image, status=message, lat=tw_lat, long=tw_long)
    json_str = json.dumps(post_media_response._json)
    json_data = json.loads(json_str)

    print("Details posted on Social Media")

    try:
        preview_link = json_data["entities"]["urls"][0]["url"]
    except:
        preview_link = "None"

    return preview_link