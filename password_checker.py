'''
    Password Checker Module
    Checks if a password has been compromised using the Pwned Passwords API
    
    Function:
        pwned_api_check(password)
    
'''

from api_utils import request_api_data
from hash_utils import get_password_leaks_count, sha1_hash

def pwned_api_check(password):
    '''
    Checks if a password has been compromised using the Pwned Passwords API.

    Args:
    password (str): The password to check.

    Returns:
    int: The count of compromised passwords for the given password.
    '''
    sha1password = sha1_hash(password)
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)
