#this file is use to instantiate intances only........

from shop import Shop
from phone import Phone

shop1 = Shop("John", 3000)

Shop.instantiate_from_csv()

# shop1.__name
print(shop1.name)

