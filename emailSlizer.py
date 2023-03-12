#Email Slizer

#collect email from user
#split the email using @ , the first part as the username, second part is gonna be saved as domain

#split domain using .

def main():
    print("welcome to my email Slizer")

    email_input=input("enter your valid email: ")

    (username, domain) =email_input.split('@')

    (domain, extend) = domain.split('.')
    print(f'username= {username}')
    print(f'domain= {domain}')
    print(f'extend= {extend}')

while True:
    main()