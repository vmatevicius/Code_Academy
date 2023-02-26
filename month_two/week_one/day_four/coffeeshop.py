import logging
from typing import Union

logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

class Restaurant():
    
    def __init__(self,name :str, drinks_menu: dict,food_menu: dict, orders: list = []):
        logging.info(f"Recieved values when creating a coffeeshop obj. name: {name}, drinks menu: {drinks_menu}, food menu {food_menu}, orders: {orders}")
        self.name = name
        self.drinks_menu = drinks_menu
        self.food_menu = food_menu
        self.orders = orders
        
    def add_order(self, order: str):
        logging.info(f"Recieved values. order {order}")
        #check if item is in the menu
        if order in self.drinks_menu or order in self.food_menu:
            self.orders.append(order)
            return f"Order added!"
        else:
            #if not return "This item is currently unavailable!"
            return f"This item is currently unavailable!"
        
    def fulfill_order(self) -> str:
        #if the orders list is not empty, return "The {item} is ready!"
        if self.orders:
            string = f"The {self.orders[0]} is ready!"
            self.orders.pop(0)
            return string
        #If the orders list is empty, return "All orders have been fulfilled!""
        else:
            return f"All orders have been fulfilled!"
        
    def list_orders(self) -> str:
        #return item/s name/s from the orders list
        if len(self.orders) > 1:
            return f'{", ".join(self.orders)}'
        else:
            return self.orders
        #if empty return an empty list
    
    def due_amount(self) -> Union[int,float]:
        #return total amount for the orders taken
        if self.orders:
            price = []
            for k, v in self.food_menu.items():
                if k in self.orders:
                    price.append(v)
                else:
                    continue
            for k, v in self.drinks_menu.items():
                if k in self.orders:
                    price.append(v)
                else:
                    continue
            return sum(price)
        else:
            return 0        
        
    def cheapest_item(self) -> str:
        #return the name of the cheapest item on the menu.
        return f"The cheapest meal is {min(self.food_menu, key=self.food_menu.get)} and the cheapest drink is {min(self.drinks_menu, key=self.drinks_menu.get)}"
        
    def drinks_only(self) -> str:
        #return names of all drinks available
        return f"Available drinks are {', '.join(self.drinks_menu.keys())}"
    
    def food_only(self) -> str:
        #return names of all food available
        return f"Available meals are {', '.join(self.food_menu.keys())}"


drinks = {
    "orange juice": 1.2,
    "lemonade": 1,
    "cranberry juice": 1.1,
    "pineapple juice": 1.5,
    "lemon iced tea": 1,
    "vanilla chai latte": 2.5,
    "hot chocolate": 3,
    "iced coffee": 3
    }

foods = {
    "tuna sandwich": 5,
    "ham and cheese sandwich": 3,
    "bacon and egg": 3,
    "steak": 8,
    "hamburger": 4,
    "cinnamon roll": 2
    }

diner = Restaurant("Cheap diner", drinks, foods)
print(diner.cheapest_item())
print(diner.add_order("hot cocoa"))
print(diner.add_order("iced coffee"))
print(diner.add_order("cinnamon roll"))
print(diner.add_order("hot chocolate"))
print(diner.list_orders())
print(diner.due_amount())
print(diner.fulfill_order())
print(diner.fulfill_order())
print(diner.fulfill_order())
print(diner.fulfill_order())
print(diner.list_orders())
print(diner.food_only())
print(diner.drinks_only())