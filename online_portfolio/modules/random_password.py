# MODULES AND LIBRARIES
from string import ascii_letters, digits
from random import choice



# RANDOM PASSWORD GENERATORS

##############################

# GENERATE RANDOM PASSWORD

##############################

def generate_random_password(length=16):

    characters = ascii_letters + digits
    password = ''.join(choice(characters) for i in range(length))

    return password