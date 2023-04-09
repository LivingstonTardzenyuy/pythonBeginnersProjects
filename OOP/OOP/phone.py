
from shop import Shop

class Phone(Shop):                          #it shows that we are inheriring Shop in the Phone class
    
    def __init__(self, name:str, price:int, quantity=0, broken_phones=0):
        
        #calling the super function (Shop) that will help us to have acccess to all the attributes of the super class
        super().__init__(
            name, price, quantity
        )
        
        
        #validations
        assert broken_phones>=0, f"the broken_phones {broken_phones} must be greater than zero"
        
        #constructor 
        self.broken_phones = broken_phones 
     

phone1= Phone('Apple', 3500, 4, 3)
phone2= Phone('Techno', 2500, 7,11)
phone3= Phone('Itel', 200, 9, 4)

# print(Shop.all)
# for items in all:
    # print(items)
# print(phone3.calculate_quantity())
print(Phone.all)