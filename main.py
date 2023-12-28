'''
    Main Checker Script
    Checks a list of passwords for compromise using the Pwned Passwords API
    
    Function:
        main(file)
    
'''
import sys
from password_checker import pwned_api_check

def main(file):
    '''
    Checks a list of passwords for compromise using the Pwned Passwords API.

    Args:
    file (str): The path to the file containing a list of passwords.

    Returns:
    str: A message indicating the completion of the password checks.
    '''
    with open(file, "r") as args:
        for line in args:
            for password in line.split():
                count = pwned_api_check(password)
                if count:
                    print(
                        f'{password} was found {count} times... you should probably change your password!')
                else:
                    print(f'{password} was NOT found. Carry on!')

    return '-----All Checks Done!-----'

if __name__ == '__main__':
    sys.exit(main(str(sys.argv[1])))
