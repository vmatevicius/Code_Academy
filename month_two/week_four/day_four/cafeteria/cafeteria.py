# Cafeteria project : Create an live menu and payment system (a.k.a console program) :

# First the program should ask if table was reserved/ not (Providing your full name) .
# And then if not would assign you a table (there is a specific number single, double or family tables) .
# After table is assigned to you, system should show how many free tables are and how which are reserved/occupied.
# The system must be able to show name/surname of the person of the reserved table (CLI option : enter reserved table nuber ; OUTCOME: Name/Surname/Time Reserved)

# After assigning table, system should show different menu options for breakfast, lunch , dinner , drinks (alcohol.
# alcohol free), to choose from. Special menu for vegetarian and vegan must be included too in the special menu.
# All menu items should have weight, preparation time in minutes, calories, and price.
# I have to have an option to change the order before the payment section. Thus I can delete, add more, update amount of the same order.

# I should be able to choose whatever I want from all menus in one ordering.
# After I finish, I need to see what I chosen, the full payable amount and approx waiting time for the food to be served

# Add an option to add tips (% from the full cost) to the final bill.

# After the payment , system should generate the receipt (logging).

from typing import Union, List, Dict, Optional
import menus as m
from abc import ABC, abstractmethod
import json


class Restaurant(ABC):
    def check_reservation(self) -> None:
        pass

    def assign_table(self) -> None:
        pass

    def show_free_tables(self) -> None:
        pass

    def show_reservation(self) -> None:
        pass

    def add_tips(self) -> None:
        pass

    @abstractmethod
    def show_menus(self) -> Dict[str, Union[float, int]]:
        pass

    @abstractmethod
    def make_order(self) -> Optional[str]:
        pass

    @abstractmethod
    def add_to_order(self) -> None:
        pass

    # @abstractmethod
    # def remove_from_order(self) -> ...:
    #     pass

    # @abstractmethod
    # def update_order_quantities(self) -> ...:
    #     pass

    # @abstractmethod
    # def show_order_summarized(self) -> ...:
    #     pass

    # @abstractmethod
    # def pay_for_order(self) -> ...:
    #     pass


# reservation:
# check if table reserved ( ask for name)
# if not assign a table ( let choose from single, double or family tables )
# implement a function that shows how many free tables and reserved tables there are( tell size of free tables)
# make a function that shows Name/Surname/Time Reserved after reserved table id is given if user want to see

# ordering:
# make a function that lets customer choose anything he wishes from menus
# Give customer options to change the order before payment( delete, add,update amount )
# after ordering is finished show full cost of the order and approx waiting time
# add an option to add tips(% from full cost)

# payment:
# implement payment
# Log the receipt using loggin


class Cafeteria(Restaurant):
    def __init__(self) -> None:
        self.menu = {
            "breakfast": m.breakfast,
            "dinner": m.dinner,
            "drinks": m.drinks,
            "lunch": m.lunch,
            "vegan": m.special_menu["Vegan"],
            "vegetarian": m.special_menu["Vegetarian"],
        }
        self.tables = {
            "single": 4,
            "double": 3,
            "family": 2,
        }
        self.reservations = {}
        self.orders = {}

    def check_reservation(self, name: str) -> bool:
        if name not in self.reservations:
            return False
        return True

    def assign_table(
        self,
        table_type: str,
        name: str,
        surname: str,
        reservation_time: Dict[str, float],
    ) -> Optional[str]:
        if self.tables[table_type] != 0:
            self.reservations = {
                name: {
                    "Surname": surname,
                    "Reservation time": reservation_time,
                    "Table": table_type,
                },
            }
            self.tables[table_type] = self.tables[table_type] - 1
        else:
            return f"There are no empty tables of this type left for today"

    def show_free_tables(self) -> str:
        if sum(self.tables.values()) == 0:
            return f"There are no empty tables left for today"
        return f"Free tables left - single: {self.tables['single']}, double: {self.tables['double']}, \
            family: {self.tables['family']}"

    def show_reserved_tables(self) -> str:
        if self.reservations == None:
            return f"There are no reservations made"
        return f"Single tables reserved: {4 - self.tables['single']}, double: {3 - self.tables['double']}, \
            family: {2 - self.tables['family']}"

    def show_reservation(self, name: str) -> str:
        if name not in self.reservations:
            return f"There is no reservation under this name"
        return f"{name} {self.reservations[name]['surname']} reserved a {self.reservations[name]['Table']} for \
            {self.reservations[name]['Reservation time']}"

    def add_tips(self, order_cost: float, tip_percentage: int) -> float:
        return order_cost + (order_cost / 100 * tip_percentage)

    def show_menus(self) -> Dict[str, Union[float, int]]:
        return json.dumps(self.menu, indent=2).replace("{", "").replace("}", "").strip()

    def make_order(
        self,
        name: str,
        alcohol: List[str] = None,
        alcohol_free: List[str] = None,
        foods: List[str] = None,
    ) -> Optional[str]:
        if alcohol == None and foods == None and alcohol_free == None:
            return f"No order has been made"
        self.orders[name] = {}
        if alcohol == None:
            pass
        else:
            for order in alcohol:
                self.orders[name][order] = dict(
                    self.menu["drinks"]["Alcohol"][order].items()
                )
        if alcohol_free == None:
            pass
        else:
            for order in alcohol_free:
                self.orders[name][order] = dict(
                    self.menu["drinks"]["Alcohol free"][order].items()
                )
        if foods == None:
            pass
        else:
            for key in self.menu.keys():
                for order in foods:
                    if order not in self.menu[key]:
                        continue
                    else:
                        self.orders[name][order] = dict(self.menu[key][order].items())

    def add_to_order(
        self,
        name: str,
        alcohol: List[str] = None,
        alcohol_free: List[str] = None,
        foods: List[str] = None,
    ) -> None:
        if alcohol == None:
            pass
        else:
            for order in alcohol:
                self.orders[name][order] = dict(
                    self.menu["drinks"]["Alcohol"][order].items()
                )
        if alcohol_free == None:
            pass
        else:
            for order in alcohol_free:
                self.orders[name][order] = dict(
                    self.menu["drinks"]["Alcohol free"][order].items()
                )
        if foods == None:
            pass
        else:
            for key in self.menu.keys():
                for order in foods:
                    if order not in self.menu[key]:
                        continue
                    else:
                        self.orders[name][order] = dict(self.menu[key][order].items())


hmmm = Cafeteria()
hmmm.make_order(
    name="Vadimas",
    alcohol=["Beer", "Vine"],
    alcohol_free=["Orange juice"],
    foods=["Steak", "Fish"],
)
hmmm.add_to_order(name="Vadimas", foods=["Grilled chicken"])
print(hmmm.orders)
