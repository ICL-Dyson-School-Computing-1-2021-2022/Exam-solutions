'''
ClassQuestion.py

Corresponding solution file for ClassQuestion.py.

NOTE: This is only one possible solution, logically
equivalent ones also acceptable.

'''

# Create a class called Trolley with one instance attribute called 'contents'
# that is created in the constructor. 
#     - 'contents' will be a dictionary and will start empty in the constructor
#        but when populated later by other methods: 
#         - the keys will be string describing the product (e.g. 'bread') 
#         - and the values will be a dictionary of two items
#                   1. the first item is 'cost' of a single product and 
#                   2. the second item is 'quantity' 
#                   (e.g. {'cost':1.50, 'quantity':3})



class Trolley:

    def __init__(self):
        self.contents = {}


# Create a method called add_product(). It should:
#   - have 3 parameters: 'product_name', 'product_cost' and 'quantity'
#   - 'quantity' has a default value of 1
#   - it should add the product to the 'contents' attribute
#        - if the product exists already, increase the quantity accordingly and ignore
#          the product_cost if different than the one already in the dictionary
#        - if the product does not already exist in the dictionary, add a new entry

    def add_product(self, product_name, product_cost, quantity = 1):
        # create a new entry in the dictionary and add the product
        self.contents[product_name]={}
        self.contents[product_name]["cost"] = product_cost
        self.contents[product_name]["quantity"] = quantity


# Create a method called remove_product(). It should:
#   - have 2 parameters: 'product_name', 'quantity'
#   - it should reduce the quantity of the product in the 'contents' attribute
#        - if the product exists already, decrease the amount by 'quantity'
#        - if the product quantity becomes 0, remove the entry from the dictionary

    def remove_product(self, product_name, quantity):
        if product_name in self.contents:
            currentValue = self.contents[product_name]["quantity"]
            
            if currentValue - quantity > 0:
                # check if the quantity drops velow zero
                self.contents[product_name]["quantity"] = currentValue - quantity
            else:
                self.contents.pop(product_name)
        else:
            print(f"there is no product {product_name}")

# Create a method called change_price(). It should:
#   - have 2 parameters: 'product_name', 'price'
#   - it should change the price of the product "product_name" to "price", in the 'contents' attribute
#   - if the product "product_name" does not exist, add a new entry to 'contents' and set 'quantity' to zero

    def change_price(self, product_name, price):
        if product_name in self.contents:
            self.contents[product_name]["cost"] = price
        else:
            self.contents[product_name]["cost"] = price
            self.contents[product_name]["quantity"] = 0
# Create a method called calculate_cost(). It should:
#   - return the total value of the trolley (cost x quantity)

    def calculate_cost(self):
        cost = 0
        for key in self.contents:
            # sum over the quantities of all the elements in contents times their respective prices
            cost += self.contents[key]["quantity"] * self.contents[key]["cost"]
        
        return cost

# Write a function called merge_trolley(). It should:
#   - have two parameters, both of which are trolley object, called 'trolley_1' and 'trolley_2'
#   - it should return a new trolley called 'other_trolley' that possesses all the items from
#     trolley_1 and trolley_2:
#       - if one entry already exists in the contents of both trolley_1 and trolley_2, 
#         sum the two quantities.
#       - if one entry that exist in both trolleys has a different price in trolley_1 than the 
#         price in trolley_2 then the function should return None and print "the two trolleys are
#         not compatible. Some prices are inconsistent.".
#       
#
# Notice that the total cost of the new created trolley should be equal to the sum of the cost
# of trolley_1 and the cost of trolley_2. Showcase that this is indeed the case by creating two
# instances of a trolley (with arbitrary items) and merge them with the function merge_trolley in 
# a new trolley. Print the cost of the three trolleys.


def merge_trolley(trolley_1, trolley_2):
    
    other_trolley = Trolley()

    for key in trolley_1.contents:
        # add the elements of trolley_1 to other_trolley
        other_trolley.add_product(key, trolley_1.contents[key]["cost"], quantity = trolley_1.contents[key]["quantity"]) 

    for key in trolley_2.contents.keys():
        # check if the elements of trolley_2 have the same value of trolley_1, if they don't, return None. If they do, add them to other_trolley.
        if key in other_trolley.contents:
            if other_trolley.contents[key]["cost"] == trolley_2.contents[key]["cost"]:
                other_trolley.contents[key]["quantity"] = other_trolley.contents[key]["quantity"] + trolley_2.contents[key]["quantity"]
            else:
                print("the two trolleys are not compatible. Some prices are inconsistent.")
                return None
        else:
            other_trolley.contents[key] = trolley_2.contents[key]
    return other_trolley

# create two trolleys and merge them

t1 = Trolley()
t2 = Trolley()
t1.add_product("bread", 1)
t1.add_product("pear", 2, quantity = 2)
t2.add_product("bread", 1)
t2.add_product("avocado", 5, quantity = 5)
t3 = merge_trolley(t1, t2)

print(f"The total cost of the first trolley is {t1.calculate_cost()}")
print(f"The total cost of the second trolley is {t2.calculate_cost()}")
print(f"The total cost of the third trolley is {t3.calculate_cost()}")

