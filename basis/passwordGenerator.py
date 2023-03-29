#helps in user registration for security

import string
import random

characters=list(string.ascii_letters + string.digits + "!@#$%^&*()_+")      # we use the ascii
def password_generator():
    while True:
        password_length=int(input("enter the password Length: "))
        random.shuffle(characters)          # to mix the characters in any format

        password=[]         #an empty list to pick any shuffle character

        for x in range(password_length):
            password.append(random.choice(characters))      #automatically select any character
        random.shuffle(password)
        password="".join(password)

        print(password)

password_generator()
