"""Bot to send admin a message on Telegram."""

from my_secrets import chat_id
from my_secrets import telegram_token

import json
import requests

# Notify administrators
def notify_admin(admin_notify_token, admin_msg, chat_id):
    """Function to advise admin when ABBIE is working."""
    def get_telegram_url(url):
        """Get the formatted url."""
        response = requests.get(url)
        content = response.content.decode("utf8")
        return content

    def send_telegram_message(admin_msg, a_chat):
        """Send the message."""
        # Compile the Telegram send message url
        send_url = URL + "sendMessage?text={}&chat_id={}".format(admin_msg, a_chat)
        get_telegram_url(send_url)


    # Update admin via Telegram
    TOKEN = admin_notify_token
    URL = "https://api.telegram.org/bot{}/".format(TOKEN)
    the_admin_msg = admin_msg
    print(the_admin_msg)

    # Send the message
    send_telegram_message(admin_msg=the_admin_msg, a_chat=chat_id)