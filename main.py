'''
This script reads configuration from a YAML file and makes a GET request to a specified API endpoint.
'''

from src.config_read import read_config
from src.data_fetcher import (
    fetch_csfloat_data,
    format_csfloat_data
)
from src.discord_bot import send_discord_message


def main():
    '''
    Main function to read config and make a GET request.
    '''
    # Read the configuration
    config, ok = read_config()
    if not ok:
        print("Failed to read configuration.")
        return
    print("Configuration loaded successfully.")

    # Make the GET request to CSFloat API
    csfloat_response, ok = fetch_csfloat_data(
        config['sites'][0]['api_url'],
        {'Authorization': config['sites'][0]['api_key']},
        config['sites'][0].get('query_params', {})
    )
    if not ok:
        print("Failed to fetch data from the API.")
        return
    print("Data fetched successfully.")

    # Format and display the fetched data
    formatted_data, ok = format_csfloat_data(
        csfloat_response,
        config['wanted_skins']
    )
    if not ok:
        print("Failed to format the fetched data.")
        return
    print("Formatted Data:", formatted_data)

    if not formatted_data:
        print("No wanted skins found.")
        return
    # Send a message to Discord if there are any wanted skins found
    ok = send_discord_message(
        config['discord']['webhook_url'],
        formatted_data
    )
    if not ok:
        print("Failed to send message to Discord.")
        return
    print("Message sent to Discord successfully.")


if __name__ == "__main__":
    main()
