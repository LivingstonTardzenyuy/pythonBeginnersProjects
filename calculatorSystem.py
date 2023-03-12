# define the functions needed: add, sub , div, mul
#print options to the user
#ask the values
#call the functions
#add while loop to continue the program until user exist

def add(numb1, numb2):
    answ=numb1+numb2
    print(answ)

def multiply(numb1, numb2):
    answ=numb1*numb2
    print(answ)

def substract(numb1, numb2):
    answ=numb1-numb2
    print(answ)

def divide(numb1, numb2):
    if numb2 == 0:
        print("Error")
    else:
        answ=numb1/numb2
        print(answ)


# multiply(numb1, numb2)
# add(numb1, numb2)
# substract(numb1, numb2)
# divide(numb1, numb2)

enter=int(input("enter the number of times you want to person calculations"))
choice=input("enter your selected choice")
i=0

while True:
    print("To add put A")
    print("To Multiply put M")
    print("To Substract put S")
    print("To Divide put D")
    print("To Exit print E")
    
    if choice == 'A' or choice =='a':
        numb1=int(input("enter first number: "))
        numb2=int(input("enter second number: "))
        add(numb1, numb2)

    elif choice == 'M' or choice =='m':
        numb1=int(input("enter first number: "))
        numb2=int(input("enter second number: "))
        multiply(numb1, numb2)


    elif choice == 'S' or choice =='s':
        numb1=int(input("enter first number: "))
        numb2=int(input("enter second number: "))
        substract(numb1, numb2)


    elif choice == 'D' or choice =='d':

        numb1=int(input("enter first number: "))
        numb2=int(input("enter second number: "))
        divide(numb1, numb2)

    elif choice == 'E' or choice == 'e':
        print("program ended")
        quit()
    
    else:
        print("No such operation")