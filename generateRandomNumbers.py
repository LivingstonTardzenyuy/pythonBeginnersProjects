#password genrator

#ask user if they want to genrate a number or not
# if yes, ask for password lenth
#generate the password and print

#if no exit

import random
def password_generator():
    # generate_random_password=True
    if generate_random_password.lower()=='T'.lower():
        length=int(input("enter the password length:"))
        i=0
        list=[]
        while i<length:
            list.append(random.randint(i,length))
            i+=1
        print(list)
    else:
        quit()
generate_random_password=input("Enter T for True or F for False")
password_generator()