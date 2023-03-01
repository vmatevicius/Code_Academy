import logging
from typing import Dict, Union, List
from menus import restaurant_menu, coffeeshop_menu
logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

class Restaurant:
    
    def __init__(self,name :str, menu: Dict[str,Dict[str,int]], orders: List[str] = []):
        logging.info(f"Recieved values when creating a coffeeshop obj. name: {name}, menu: {menu}, orders: {orders}")
        if not name or type(name) != str:
            logging.error("Error recieved because there was no name or type of name was wrong")
        self.name: str = name
        if type(menu) != dict:
            logging.error("Error recieved because variable menu is not a dictionary")
        self.menu: Dict[str,Dict[str,int]] = menu
        self.orders: List[str] = orders
        
    def add_order(self, order: str) -> str:
        logging.info(f"Recieved values. order {order}")
        if order in self.menu["drinks"] or order in self.menu["foods"]:
            self.orders.append(order)
            return f"Order added!"
        return f"This item is currently unavailable!"

        
    def fulfill_order(self) -> str:
        if not self.orders:
            return f"All orders have been fulfilled!"
        string = f"The {self.orders[0]} is ready!"
        self.orders.pop(0)
        return string
        
    def list_orders(self) -> str:
        if len(self.orders) > 1:
            return f'{", ".join(self.orders)}'
        return self.orders[0]
    
    def due_amount(self) -> Union[int,float]:
        if not self.orders:
            return 0
        prices = 0
        for order in self.orders:
            if order in self.menu["drinks"]:
                prices = prices + self.menu["drinks"][order]
            else:
                prices = prices + self.menu["foods"][order]
        return prices       
        
    def cheapest_item(self) -> str:
        return f"The cheapest meal is {min(self.menu['foods'], key=self.menu['foods'].get)} and the cheapest drink is {min(self.menu['drinks'], key=self.menu['drinks'].get)}"
        
    def drinks_only(self) -> str:
        return f"Available drinks are {', '.join(self.menu['drinks'].keys())}"
    
    def food_only(self) -> str:
        return f"Available meals are {', '.join(self.menu['foods'].keys())}"

class CoffeeShop(Restaurant):
    
    def __init__(self, name: str ,menu: Dict[str,int], orders: List[str] = []):
        super().__init__(name, menu, orders)
    
    def cheapest_item(self) -> str:
        return f"The cheapest drink is {min(self.menu, key=self.menu.get)}"
    
    def add_order(self, order: str) -> str:
        logging.info(f"Recieved values. order {order}")
        if order in self.menu:
            self.orders.append(order)
            return f"Order added!"
        return f"This item is currently unavailable!"