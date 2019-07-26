# A.B.B.I.E. Social Media Posting Bot

**A bot that extracts content from Google Sheets and posts on different social media platforms.**

Written in Python 3.6.8 🐍

Running on Ubuntu 18.04

---

## Sprints

* #01 - Facebook integration

* #02 - Pinterest integration

---

## Table of contents

1. [Requirements](https://github.com/rocketmovingapp/abbie_social_post_bot#requirements)
2. [Quickstart](https://github.com/rocketmovingapp/abbie_social_post_bot#quickstart)
3. [Contributors](https://github.com/rocketmovingapp/abbie_social_post_bot#contributors)
4. [Disclaimer](https://github.com/rocketmovingapp/abbie_social_post_bot#disclaimer)

---

## [Requirements](#requirements)

* <strong>Virtual Environment</strong> (Optional)
 ```bash
python3 -m venv venv
 ```

* <strong>Requests</strong>: Install the requests library.
 ```bash
sudo pip3 install requests
 ```

* <strong>Google Client Library</strong>: Install the [Google Client Library](https://developers.google.com/sheets/api). A Google Cloud Console account will be required to access Google's APIs. Add the 'client_secrets.json' file to the main directory.
 ```bash
sudo pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
 ```

* <strong>Google Sheets</strong>: A Google Sheet with data is required. Store content such as 'post text', 'post image', and 'post hashtags' for the bot to extract rom Google Sheets.

* <strong>Google Geocode API Key</strong>: Check the [Google Maps Platforn Documentation](https://developers.google.com/maps/documentation/geocoding/start) for more information.

* <strong>Pixabay API Key</strong>: Check the [Pixabay API Documentation](https://pixabay.com/api/docs) for more information.

* <strong>Pillow</strong>: Install the [Pillow](https://www.pillow.readthedocs.io/en/stable) library.
```bash
pip install Pillow
```

* <strong>Instapy-CLI</strong>: Install the [Instapy-CLI](https://github.com/instagrambot/instapy-cli) library.
```bash
sudo pip3 install instapy-cli
```

* <strong>Telegrm Bot</strong>: Create an account with [Telegram](https://telegram.org/) and use [BotFather](https://telegram.me/botfather) to create the Telegram bot framework.

* <strong>Tweepy</strong>: Install the [Tweepy](https://www.tweepy.org) library.
```bash
sudo pip install tweepy
```

---

## [Quickstart](#quickstart)

**Instagram modules**

```bash
python3 ig_main.py
```
This module posts references content in Google Sheets, posts the content on Instagram, and sends the administrator a link to the post, via Telegram. 
*Edit the filepaths in the code to match those of your machine/config.*

---

## [Contributors](#contributors)

Eduardo: IG [@_eduardo_py](https://www.instagram.com/_eduardo_py)
Lucas: IG [@lucas09](https://www.instagram.com/lucas039)

Tell us what you think! [@rocketmovingapp](https://www.instagram.com/rocketmovingapp)

---

## Disclaimer

This tool is for educational purposes only. Use at your own risk.