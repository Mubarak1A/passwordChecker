'''
    Password Hasing Module
    Help to hash hash password to enhance security
    
    Functions:
        - get_password_leaks_counts()
        - sha1_hash()
'''

import hashlib

def get_password_leaks_count(hashes, hash_to_check):
    '''
    Parses the response from the Pwned Passwords API and returns the count of compromised passwords.

    Args:
    hashes (requests.Response): The response object from the API.
    hash_to_check (str): The remaining part of the SHA-1 hash to check.

    Returns:
    int: The count of compromised passwords for the given hash.
    '''
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for hash, count in hashes:
        if hash == hash_to_check:
            return count
    return 0

def sha1_hash(password):
    '''
    Generates the SHA-1 hash for a given password.

    Args:
    password (str): The password to hash.

    Returns:
    str: The SHA-1 hash of the password.
    '''
    return hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
