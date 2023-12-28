'''
    Api Utility Module
    Help get password data from API
    
    Function:
        request_api_data(query)
'''

import requests

def request_api_data(query):
    '''
    Requests data from the Pwned Passwords API for a given hash prefix.

    Args:
    query (str): The first 5 characters of the SHA-1 hash of a password.

    Returns:
    requests.Response: The response object from the API.

    Raises:
    RuntimeError: If the API request fails (status code other than 200).
    '''
    url = 'https://api.pwnedpasswords.com/range/' + query
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, check the API URL and try again!')
    return res
