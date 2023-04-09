
import csv

class Shop:
    pay_rate = 0.8          #a class attribute declaring the payrate
    
    all=[] 
       
    def __init__(self, name: str, price: int, quantity =0):
        
        
        #validation 
        assert price >=0, f"Price {price} The price must be greater than zero"
        assert quantity >=0, f"The quantity {quantity} must be greater than zero"
        
        self.__name = name              #private attributes
        self.quantity = quantity
        self.price = price
        # print("All the itemts in the shop")
        
        @property
        def name(self):
            return self.__name
        
        #   actions to execute
        Shop.all.append(self)       #helps to append all the intances once created
        
    def calculate_quantity(self):
        return self.price * self.quantity
    
    def discount(self):
        self.price = self.price * self.pay_rate

    @classmethod        #using decorators to change the behavior of the future
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            #instantiating all the attributes in the Shop class...
            Shop(                                                   
                name = item.get('name'),
                price = int(item.get('price')),
                quantity = int(item.get('quantity')),
            )
    
    # @property           # is used to create read only attributes hence encapsulation.... 
    # def read_only_name(self):
        # return 'BBB'
    
    def __repr__(self):         #to represent the string representaion of an object
        return f"({self.__class__.__name__}'{self.name}', '{self.quantity}', '{self.price}')"           #self.__class__name is use to access the name of a class from the instance level...
  

  
Shop.instantiate_from_csv()     #creating an intance of the csv

shop1= Shop('K_shop', 200, 5)    
# print(Shop.all)

