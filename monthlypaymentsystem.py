#interest rate monthly payment calculator

#collect the necessary inputs: principal, apr(annual interest rate, years(years to pay the loan)
#calculate the monthly payment
#show to the user

# while True:
def monthly_payment_calculator(principal,interest_rate,years):
    amount_of_months=years*12
    monthly_payment=principal*amount_of_months/(1-(1+amount_of_months)**(-interest_rate))
    print("the monthly payment for this loan is %.2f" % monthly_payment)
principal=int(input("Enter the principal Amount: "))
interest_rate=float(input("Enter the interest rate: "))
years=int(input("Enter the years to pay the interest: "))

monthly_payment_calculator(principal, interest_rate, years)