"""Module to interact with Twitter via Tweepy."""

from my_secrets import app_id
from my_secrets import app_secret
from my_secrets import long_token
from my_secrets import page_id
from my_secrets import parent_object
from my_secrets import permanent_key
from my_secrets import permanent_token
from my_secrets import user_short_token

import facebook
import requests




page_access_token = long_token
graph = facebook.GraphAPI(page_access_token)
facebook_page_id = page_id
graph.put_object(parent_object, "feed", message="Don't you just love API calls?!")