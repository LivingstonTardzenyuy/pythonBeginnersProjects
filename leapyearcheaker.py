# leap year

def is_leap_yar(year):
    if year%4  == 0:
        if year % 100 ==0:
            if year % 400==0:
                print("leap year")
            else:
                print("not a leap year")
        else:
            print("Leap year")
    else:
        print("Not a leap year")
input=int(input("enter a year: "))
is_leap_yar(input)