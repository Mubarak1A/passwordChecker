# Password Checker Script

The Password Checker Script is a Python tool designed to check the security of passwords by consulting the Pwned Passwords API. This script allows users to evaluate if a password has been compromised in previous data breaches.

## Overview

The script is divided into several modules to enhance code organization and maintainability:

- `api_utils.py`: Contains functions related to making requests to the Pwned Passwords API.
- `hash_utils.py`: Includes functions for hash-related operations, such as generating SHA-1 hashes.
- `password_checker.py`: Implements the main logic for checking passwords against the Pwned Passwords API.
- `main.py`: The main script that interacts with user input and executes the password checks.

## Modules

### `api_utils.py`

This module provides utilities for interacting with the Pwned Passwords API.

- **`request_api_data(query)`**
  - Requests data from the Pwned Passwords API for a given hash prefix.
  - Args:
    - `query` (str): The first 5 characters of the SHA-1 hash of a password.
  - Returns:
    - `requests.Response`: The response object from the API.
  - Raises:
    - `RuntimeError`: If the API request fails (status code other than 200).

### `hash_utils.py`

This module handles operations related to password hashing.

- **`get_password_leaks_count(hashes, hash_to_check)`**
  - Parses the response from the Pwned Passwords API and returns the count of compromised passwords.
  - Args:
    - `hashes` (`requests.Response`): The response object from the API.
    - `hash_to_check` (str): The remaining part of the SHA-1 hash to check.
  - Returns:
    - `int`: The count of compromised passwords for the given hash.
- **`sha1_hash(password)`**
  - Generates the SHA-1 hash for a given password.
  - Args:
    - `password` (str): The password to hash.
  - Returns:
    - `str`: The SHA-1 hash of the password.

### `password_checker.py`

This module contains the core logic for checking passwords against the Pwned Passwords API.

- **`pwned_api_check(password)`**
  - Checks if a password has been compromised using the Pwned Passwords API.
  - Args:
    - `password` (str): The password to check.
  - Returns:
    - `int`: The count of compromised passwords for the given password.

### `main.py`

The main script orchestrates the password checking process.

- **`main(file)`**
  - Checks a list of passwords for compromise using the Pwned Passwords API.
  - Args:
    - `file` (str): The path to the file containing a list of passwords.
  - Returns:
    - `str`: A message indicating the completion of the password checks.

## Usage

1. **Clone Script Repo:**
   - ```git clone https://github.com/Mubarak1A/passwordChecker.git```

2. **Environment Setup:**
   - Make sure you have Python 3 installed on your system.

3. **Install Dependencies:**
   - Install required dependencies using the following command:

     ```bash
     pip install requests
     ```

4. **Sample File Content:**
   - Customize the sample passwords by modifying the ```sample.txt`` file. The script reads the content from thi
     file and execute the main function base on the passwords in the file.

5. **Run the Script:**
   - Execute the script using the following command:

     ```bash
     python3 main.py <path_to_password_file>
     ```

     Replace `<path_to_password_file>` with the path to the file containing a list of passwords.

## Important Notes

- Ensure that the Pwned Passwords API server allows requests from your environment.
- Use secure methods for handling and storing sensitive information, such as credentials.

Feel free to customize the script or modules based on your specific use case and security requirements.