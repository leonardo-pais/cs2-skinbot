'''
Sends a message to a Discord channel using a webhook.
'''

import requests # pylint: disable=import-error


def send_discord_message(webhook_url: str, message: str) -> bool:
    '''
    Sends a message to a Discord channel using a webhook.
    Args:
        webhook_url (str): Discord webhook URL.
        message (str): Message to send.
    Returns:
        bool: Returns True if the message was sent successfully, False otherwise.
    '''
    payload = {"content": message}
    r = requests.post(webhook_url, json=payload)
    if r.status_code != 204:
        print(f"Failed to delivery: {r.status_code} - {r.text}")
        return False
    return True
