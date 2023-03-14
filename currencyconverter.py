#currency converted program

def main():
    print("This program converts US dollars to Pounds Sterling")
    print()

    dollars=float(input("Enter the amount in Dollars"))
    pounds=convert_to_pounds(dollars)
    print("that is " + str(pounds) + "pounds")

convert_to_pounds=lambda dollars: dollars*0.82

main()