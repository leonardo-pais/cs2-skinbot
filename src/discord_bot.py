'''
Sends a message to a Discord channel using a webhook.
'''

from typing import Any, Dict, Tuple
import requests # pylint: disable=import-error


def send_discord_message(webhook_url: str, data: Tuple[Dict[Any, Any]]) -> bool:
    '''
    Sends a formatted message to a Discord channel using a webhook.
    Args:
        webhook_url (str): Discord webhook URL.
        data (tuple): Tuple of dicts to format and send.
    Returns:
        bool: Returns True if the message was sent successfully, False otherwise.
    '''
    message = ""
    for item in data:
        for key, value in item.items():
            message += f"**{key}:** {value}\n"
        message += "\n"

    payload = {
        "embeds": [
            {
                "title": "New Skins Found!",
                "description": message,
                "color": 5814783
            }
        ]
    }
    try:
        r = requests.post(webhook_url, json=payload)
        if r.status_code != 204:
            print(f"Failed to send: {r.status_code} - {r.text}")
            return False
        return True
    except Exception as e:
        print(f"Error during request: {e}")
        return False
