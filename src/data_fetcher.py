'''
Module for fetching data from external APIs.
'''

from typing import Any, Dict, Tuple
import requests # pylint: disable=import-error


def fetch_csfloat_data(
        url: str,
        headers: Dict[Any, Any],
        params: Dict[Any, Any]) -> Tuple[Dict[Any, Any], bool]:
    '''
    Fetch data from the given URL with optional headers and parameters.

    Args:
        url (str): The API endpoint URL.
        headers (dict, optional): Headers to include in the request.
        params (dict, optional): Query parameters for the request.

    Returns:
        dict: The JSON response from the API if the request is successful.
        bool: Reun True if the request was successful, False otherwise.
    '''

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        data: Dict = response.json()
        print(f'Data fetched: {data}')

    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return {}, False

    return data, True


def format_csfloat_data(
       csfloat_data: Dict[Any, Any],
       wanted_skins: Dict[Any, Any]
       ) -> Tuple[Dict[Any, Any], bool]:
    '''
    Format the data fetched from CSFloat API.
    Args:
        csfloat_data (dict): The raw data fetched from the CSFloat API.
        wanted_skins (list): List of skins to filter the data.
    Returns:
        dict: Formatted data containing only the wanted skins.
        bool: Returns True if formatting was successful, False otherwise.
    '''
    formatted_data: Dict[Any, Any] = {}
    try:
        for item in csfloat_data['data']:
            if item['item']['item_name'] in wanted_skins:
                formatted_data[item['item']['item_name']] = [
                    item['item']['float_value'],
                    item['price'],
                    item['item']['inspect_link']
                    ]
    except Exception as e:
        print(f"Error formatting data: {e}")
        return {}, False
    return formatted_data, True
