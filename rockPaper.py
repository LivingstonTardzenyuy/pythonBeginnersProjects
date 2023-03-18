#rock paper scissors game

import random


exit=False
user_point=0
computer_point=0

while exit==False:
    user_input = input("Choose rock, paper, scissors or exit: ")
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)

    if user_input=='exit'.lower():
        print("Game over")
        exit=True

    if user_input=='rock':
        if computer_choice=='rock':
            print("Your input is rock")
            print("Computer input is rock")
            print("it is a tie!")

        elif computer_choice=="paper":
            print("your input is rock")
            print("computer input is paper")
            print("The computer wins")
            computer_point+=1
            print(computer_point)

        else:
            print("your input is rock")
            print("computer input is paper")
            print("you  wins")
            user_input += 1
            print(user_point)

    elif user_input == 'paper':
        if computer_choice == 'rock':
            print("Your input is paper")
            print("Computer input is rock")
            print("you win!")
            user_input+=1
            print(user_input)

        elif computer_choice == "paper":
            print("Your input is rock")
            print("Computer input is paper")
            print("it is a tie!")

        else:
            print("your input is paper")
            print("computer input is scissors")
            print("The computer wins")
            computer_point += 1
            print(computer_point)


    else:
        if computer_choice == 'rock':
            print("Your input is paper")
            print("Computer input is rock")
            print("you win!")
            computer_point+=1
            print(computer_point)
        elif computer_choice == "paper":
            print("your input is paper")
            print("computer input is scissors")
            print("The computer wins")
            computer_point += 1
            print(computer_point)

        else:
            print("Your input is rock")
            print("Computer input is paper")
            print("it is a tie!")


