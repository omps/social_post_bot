"""Module to interact with Google Maps Geocode API."""

from my_secrets import ggeocode as GEOCODE_API_KEY
import json
import requests

def get_location_coordinates(location):
    """Get the lat and long coordinates for the location."""
    # Replace the "," with a "+"
    address = location.replace(",", "+")

    # Define the base url
    geo_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={GEOCODE_API_KEY}"
    response = requests.get(geo_url)
    content = response.content.decode("utf8")
    geo_js = json.loads(content)
    geo_status = geo_js["status"]

    if geo_status == "OK":
        geo_elements = geo_js["results"][0]
        geometry = geo_elements["geometry"]
        location_coordinates = geometry["location"]
        location_lat = location_coordinates["lat"]
        location_long = location_coordinates["lng"]
        print(f"Long/lat coordinates successfully extracted.")
    else:
        location_lat = "Unavailable"
        location_long = "Unavailable"
        print(f"Long/lat coordinates unavailable.")

    return location_lat, location_long