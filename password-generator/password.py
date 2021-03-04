# Import string library to store letters, digits, and punctuation

import string
import random

LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation

# Create function to receive password length

def get_password_length():
    length = input("How long do you want your password to be: ")
    return int(length)

# Define parameter length that defaults to 8 because the minimum length of a strong password is 8 characters long

def password_generator(length=8):

    # Create alphanumerical from string constants
    printable = f'{LETTERS}{NUMBERS}{PUNCTUATION}'

    # Convert printable from string to list and shuffle
    printable = list(printable)
    random.shuffle(printable)

    # Generate random passwords and convert to string
    random_password = random.choices(printable, k=length)
    random_password = ''.join(random_password)
    return random_password
    
    # Creating password with the default length of 8 characters
    password_a = password_generator()


    # Creating password with user's designated input for length
    password_length = get_password_length()
    password_b = password_generator(password_length)

    print("password a (" + str(len(password_a)) + "):\t\t" + password_a )
    print("password b (" + str(len(password_b)) + "):\t\t" + password_b )
    

