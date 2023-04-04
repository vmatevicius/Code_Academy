from typing import Union, Dict, Optional, List
import dictionaries as d
import helpers as h
from datetime import datetime


class Menu:
    def __init__(self) -> None:
        self.alcohol = d.DRINKS["Alcohol"]
        self.alcohol_free = d.DRINKS["Alcohol free"]
        self.breakfast = d.BREAKFAST
        self.lunch = d.LUNCH
        self.dinner = d.DINNER
        self.vegan = d.SPECIAL_MENU["Vegan"]
        self.vegetarian = d.SPECIAL_MENU["Vegetarian"]

    def show_menus(self) -> Dict[str, Union[float, int]]:
        current_time = int(datetime.now().strftime("%H"))
        h.print_menu(submenu_name=self.alcohol)
        h.print_menu(submenu_name=self.alcohol_free)
        h.print_menu(submenu_name=self.vegetarian)
        h.print_menu(submenu_name=self.vegan)

        if 12 < current_time < 18:
            h.print_menu(submenu_name=self.lunch)
        if 12 > current_time:
            h.print_menu(submenu_name=self.breakfast)
        if 18 < current_time:
            h.print_menu(submenu_name=self.dinner)


class Reservation:
    def __init__(
        self, name: str, surname: str, time: str, table_type: str, table_id: int
    ) -> None:
        self.name = name
        self.surname = surname
        self.time = time
        self.table_type = table_type
        self.table_id = table_id


class Tables:
    def __init__(self) -> None:
        self.tables = {
            "single": d.SINGLE_TABLES,
            "double": d.DOUBLE_TABLES,
            "family": d.FAMILY_TABLES,
        }
        self.table_reservations: List[Reservation] = []

    def check_reservation(self, name: str, surname: str) -> bool:
        if self.table_reservations == None:
            return False
        for reservation in self.table_reservations:
            if reservation.name == name and reservation.surname == surname:
                return True

    def check_if_table_free(self, table_type: str, table_id: int) -> bool:
        if self.tables[table_type][table_id] == "free":
            return True
        return False

    def reserve_table(
        self, name: str, surname: str, time: str, table_type: str, table_id: int
    ) -> Optional[str]:
        if self.check_if_table_free(table_type=table_type, table_id=table_id):
            reservation = Reservation(
                name=name,
                surname=surname,
                time=time,
                table_type=table_type,
                table_id=table_id,
            )
            self.table_reservations.append(reservation)
            self.tables[table_type][table_id] = "reserved"
        else:
            return f"Table is already reserved"

    def show_free_tables(self) -> None:
        for key, value in self.tables.items():
            for table_id, table_state in value.items():
                if table_state == "free":
                    print(f"{key}: {table_id} is {table_state}")

    def show_reserved_tables(self) -> str:
        for key, value in self.tables.items():
            for table_id, table_state in value.items():
                if table_state == "reserved":
                    print(f"{key}: {table_id} is {table_state}")

    def show_reservation(self, name: str, surname: str) -> str:
        if self.table_reservations == None:
            return f"We are sorry, reservation was not found"
        for reservation in self.table_reservations:
            if reservation.name == name and reservation.surname == surname:
                return f"{name} {surname} reserved a {reservation.table_type} type table for {reservation.time} o'clock"
            else:
                return f"We are sorry, reservation was not found"


class Order:
    def __init__(
        self,
        name: str,
        surname: str,
        foods: Dict[str, int],
        alcohol: Dict[str, int] = None,
        alcohol_free: Dict[str, int] = None,
    ) -> None:
        self.name = name
        self.surname = surname
        self.foods = foods
        self.alcohol = alcohol
        self.alcohol_free = alcohol_free


class Orders:
    def __init__(self) -> None:
        self.orders: List[Orders] = []

    def make_order(
        self,
        name: str,
        surname: str,
        foods: Dict[str, int],
        alcohol: Dict[str, int] = None,
        alcohol_free: Dict[str, int] = None,
    ):
        if alcohol != None and alcohol_free != None:
            self.orders.append(Order(name, surname, foods, alcohol, alcohol_free))
        if alcohol != None:
            self.orders.append(Order(name, surname, foods, alcohol))
        if alcohol_free != None:
            self.orders.append(Order(name, surname, foods, alcohol_free))
        else:
            order = Order(name, surname, foods)
            self.orders.append(order)

    def add_to_order(
        self,
        name: str,
        surname: str,
        alcohol: Dict[str, int] = None,
        alcohol_free: Dict[str, int] = None,
        foods: Dict[str, int] = None,
    ) -> None:
        if alcohol == None:
            pass
        else:
            for order in self.orders:
                if order.name == name and order.surname == surname:
                    order.alcohol.update(alcohol)
        if alcohol_free == None:
            pass
        else:
            for order in self.orders:
                if order.name == name and order.surname == surname:
                    order.alcohol_free.update(alcohol_free)
        if foods == None:
            pass
        else:
            for order in self.orders:
                if order.name == name and order.surname == surname:
                    order.foods.update(foods)

    def remove_from_order(self):
        pass

    def update_order_quantities(self):
        pass

    def show_order_summarized(self):
        pass

    def show_order_cost(self):
        pass


#

#     def remove_from_order(self, full_name: str, what_to_remove: str) -> None:
#         del self.orders[full_name][what_to_remove]

#     def update_order_quantities(
#         self,
#         full_name: str,
#         alcohol: Dict[str, int] = None,
#         alcohol_free: Dict[str, int] = None,
#         foods: Dict[str, int] = None,
#     ) -> None:
#         if alcohol == None:
#             pass
#         else:
#             for key, value in alcohol.items():
#                 self.orders[full_name][key]["quantity"] = value
#         if alcohol_free == None:
#             pass
#         else:
#             for key, value in alcohol_free.items():
#                 self.orders[full_name][key]["quantity"] = value
#         if foods == None:
#             pass
#         else:
#             for key, value in foods.items():
#                 self.orders[full_name][key]["quantity"] = value

#     def add_to_order_quantities(
#         self,
#         full_name: str,
#         alcohol: Dict[str, int] = None,
#         alcohol_free: Dict[str, int] = None,
#         foods: Dict[str, int] = None,
#     ):
#         if alcohol == None:
#             pass
#         else:
#             for key, value in alcohol.items():
#                 self.orders[full_name][key]["quantity"] += value
#         if alcohol_free == None:
#             pass
#         else:
#             for key, value in alcohol_free.items():
#                 self.orders[full_name][key]["quantity"] += value
#         if foods == None:
#             pass
#         else:
#             for key, value in foods.items():
#                 self.orders[full_name][key]["quantity"] += value

#     def subtract_from_order_amounts(
#         self,
#         full_name: str,
#         alcohol: Dict[str, int] = None,
#         alcohol_free: Dict[str, int] = None,
#         foods: Dict[str, int] = None,
#     ):
#         if alcohol == None:
#             pass
#         else:
#             for key, value in alcohol.items():
#                 amount = self.orders[full_name][key]["quantity"]
#                 self.orders[full_name][key]["quantity"] = amount - value
#                 if self.orders[full_name][key]["quantity"] == 0:
#                     del self.orders[full_name][key]
#         if alcohol_free == None:
#             pass
#         else:
#             for key, value in alcohol_free.items():
#                 amount = self.orders[full_name][key]["quantity"]
#                 self.orders[full_name][key]["quantity"] = amount - value
#                 if self.orders[full_name][key]["quantity"] == 0:
#                     del self.orders[full_name][key]
#         if foods == None:
#             pass
#         else:
#             for key, value in foods.items():
#                 amount = self.orders[full_name][key]["quantity"]
#                 self.orders[full_name][key]["quantity"] = amount - value
#                 if self.orders[full_name][key]["quantity"] == 0:
#                     del self.orders[full_name][key]

#     def show_order_summarized(self, full_name: str) -> None:
#         total_cost = self.show_order_cost(full_name=full_name)
#         ordered_things = {}
#         for key, value in self.orders[full_name].items():
#             for inner_key, inner_value in self.orders[full_name][key].items():
#                 if inner_key == "quantity":
#                     ordered_things[key] = inner_value
#                 else:
#                     continue
#         print(f"Total cost is: {total_cost}")
#         print("Your order is:")
#         for key, value in ordered_things.items():
#             print(f"{key}, amount: {value}")

#     def show_order_cost(self, full_name: str) -> None:
#         cost = 0
#         for key in self.orders[full_name].keys():
#             quantity = self.orders[full_name][key]["quantity"]
#             cost = cost + (self.orders[full_name][key]["price"] * quantity)
#         return cost


# class Payment:
#     def __init__(self) -> None:
#         pass

#     def add_tips(self, tip_percentage: int, order_cost: float = None) -> float:
# #         return order_cost + (order_cost / 100 * tip_percentage)


# table = Tables()
# table.show_free_tables()
# table.reserve_table(
#     name="Anton", surname="Nezinosi", time="13:00", table_type="single", table_id=2
# )
# print("\n")
# table.show_free_tables()
# print(
#     table.reserve_table(
#         name="Anton", surname="Nezinosi", time="13:00", table_type="single", table_id=2
#     )
# )
# table.show_reserved_tables()
# print(table.show_reservation(name="Anton", surname="Nezinosi"))

# menu = Menu()
# menu.show_menus()
