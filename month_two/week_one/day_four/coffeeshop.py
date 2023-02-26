import logging

logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

# menu : a list of items (of dict type), with each item containing the item (name of the item), type (whether a food or a drink) and price.
# orders : an empty list
# IMPORTANT: Orders are fulfilled in a FIFO (first-in, first-out) order. Examples:

class CoffeeShop():
    
    def __init__(self,name :str, menu: dict, orders: list):
        logging.info(f"Recieved values when creating a coffeeshop obj. name: {name}, menu: {menu}, orders: {orders}")
        self.name = name
        self.menu = menu
        self.orders = orders
        
    def add_order():
        #check if item is in the menu
        #if in menu add to the orders list
        #if not return "This item is currently unavailable!"
        ...
    
    def fulfill_order():
        #if the orders list is not empty, return "The {item} is ready!"
        #If the orders list is empty, return "All orders have been fulfilled!""
        ...
        
    def list_orders():
        #return item/s name/s from the orders list
        #if empty return an empty list
        ...
    
    def due_amount():
        #return total amount for the orders taken
        #if no orders return 0     
        ...
        
    def cheapest_item():
        #Return the name of the cheapest item in the menu
        ...
        
    def drinks_only():
        #return names of all drinks available
        ...
    
    def food_only():
        #return names of all food available
        ...