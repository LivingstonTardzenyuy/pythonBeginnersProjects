#import random
#define function to rool dice
#draw a dictionary that will have the drawings of the dice
#a loop

import random
def rool_dice():
    roll=input("Roll the dice (Yes/No): ")
    while roll.lower()=="Yes".lower():
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)

        print("dice rolled: {} and {}".format(dice1,dice2))

        roll=input("Roll again: (Yes/No): ")

rool_dice()