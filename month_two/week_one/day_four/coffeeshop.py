import logging
from typing import Dict, Union, List

logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

class Restaurant:
    
    def __init__(self,name :str, menu: Dict[str, List[Dict[str, Union[int, float]]]], orders: List[str] = []):
        logging.info(f"Recieved values when creating a coffeeshop obj. name: {name}, menu: {menu}, orders: {orders}")
        if not name or type(name) != str:
            logging.error("Error recieved because there was no name or type of name was wrong")
            raise ValueError("No value or wrong input type")
        self.name: str = name
        if type(menu) != dict:
            logging.error("Error recieved because menu must be a dictonary")
            raise ValueError("Menu must be a dictionary")
        self.__menu: Dict[str, List[Dict[str, Union[int, float]]]] = menu
        self.orders: List[str] = orders
        
    def add_order(self, order: str):
        logging.info(f"Recieved values. order {order}")
        #check if item is in the menu
        if order in self.__menu["drinks"] or order in self.__menu["foods"]:
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
            prices = 0
            for order in self.orders:
                if order in self.__menu["drinks"]:
                    prices = prices + self.__menu["drinks"][order]
                else:
                    prices = prices + self.__menu["foods"][order]
            return prices
        else:
            return 0        
        
    def cheapest_item(self) -> str:
        #return the name of the cheapest item on the menu.
        return f"The cheapest meal is {min(self.__menu['foods'], key=self.__menu['foods'].get)} and the cheapest drink is {min(self.__menu['drinks'], key=self.__menu['drinks'].get)}"
        
    def drinks_only(self) -> str:
        #return names of all drinks available
        return f"Available drinks are {', '.join(self.__menu['drinks'].keys())}"
    
    def food_only(self) -> str:
        #return names of all food available
        return f"Available meals are {', '.join(self.__menu['foods'].keys())}"

class CoffeeShop(Restaurant):
    
    def __init__(self, name: str ,menu, orders: list = []):
        self.name = name
        self.menu = menu
        self.orders = orders
    
    def cheapest_item(self) -> str:
        #return the name of the cheapest item on the menu.
        return f"The cheapest drink is {min(self.menu, key=self.menu.get)}"
    

coffeeshop_menu = {
    "orange juice": 1.2,
    "lemonade": 1.8,
    "cranberry juice": 1.1,
    "pineapple juice": 1.5,
    "lemon iced tea": 1.6,
    "vanilla chai latte": 2.5,
    "hot chocolate": 3,
    "iced coffee": 3
   }


coffeeshop = CoffeeShop("Caffeine", coffeeshop_menu)
print(coffeeshop.cheapest_item())

# restaurant_menu = {
#    "drinks": {
#         "orange juice": 1.2,
#         "lemonade": 1.8,
#         "cranberry juice": 1.1,
#         "pineapple juice": 1.5,
#         "lemon iced tea": 1.6,
#         "vanilla chai latte": 2.5,
#         "hot chocolate": 3,
#         "iced coffee": 3
#    },
#     "foods": {
#         "tuna sandwich": 5,
#         "ham and cheese sandwich": 3,
#         "bacon and egg": 3,
#         "steak": 8,
#         "hamburger": 4,
#         "cinnamon roll": 2
#     }
#     }

# coffee_shop = Restaurant("Cheap diner", restaurant_menu)
# print(coffee_shop.cheapest_item())
# print(coffee_shop.add_order("lemonade"))
# print(coffee_shop.add_order("cinnamon roll"))
# print(coffee_shop.add_order("hot chocolate"))
# print(coffee_shop.list_orders())
# print(coffee_shop.due_amount())
# print(coffee_shop.fulfill_order())
# print(coffee_shop.fulfill_order())
# print(coffee_shop.fulfill_order())
# print(coffee_shop.fulfill_order())
# print(coffee_shop.list_orders())
# print(coffee_shop.food_only())
# print(coffee_shop.drinks_only())

coffeeshop_menu = {
   "drinks": {
        "orange juice": 1.2,
        "lemonade": 1.8,
        "cranberry juice": 1.1,
        "pineapple juice": 1.5,
        "lemon iced tea": 1.6,
        "vanilla chai latte": 2.5,
        "hot chocolate": 3,
        "iced coffee": 3
   }
}