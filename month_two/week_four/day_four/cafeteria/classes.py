from typing import Union, Dict, Optional
import menus as m
import json


class Reservation:
    def __init__(self) -> None:
        self.tables = {
            "single": 4,
            "double": 3,
            "family": 2,
        }
        self.reservations = {}

    def check_reservation(self, full_name: str) -> bool:
        if full_name not in self.reservations:
            return False
        return True

    def assign_table(
        self,
        table_type: str,
        full_name: str,
        reservation_time: Dict[str, float],
    ) -> Optional[str]:
        if self.tables[table_type] != 0:
            self.reservations = {
                full_name: {
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
        return f"Free tables left - single: {self.tables['single']}, double: {self.tables['double']}, family: {self.tables['family']}"

    def show_reserved_tables(self) -> str:
        max_single_tables = 4
        max_double_tables = 3
        max_family_tables = 2
        if self.reservations == None:
            return f"There are no reservations made"
        return (
            f"Single tables reserved: {max_single_tables - self.tables['single']}, double:"
            f"{max_double_tables - self.tables['double']}, family: {max_family_tables - self.tables['family']}"
        )

    def show_reservation(self, full_name: str) -> str:
        if full_name not in self.reservations:
            return f"There is no reservation under this name"
        return (
            f"{full_name} reserved a"
            f" '{self.reservations[full_name]['Table']}' table for {self.reservations[full_name]['Reservation time']} o'clock"
        )


class Order:
    def __init__(self) -> None:
        self.orders = {}
        self.menu = {
            "breakfast": m.breakfast,
            "dinner": m.dinner,
            "drinks": m.drinks,
            "lunch": m.lunch,
            "vegan": m.special_menu["Vegan"],
            "vegetarian": m.special_menu["Vegetarian"],
        }

    def show_menus(self) -> Dict[str, Union[float, int]]:
        return json.dumps(self.menu, indent=2).replace("{", "").replace("}", "").strip()

    def make_order(
        self,
        full_name: str,
        alcohol: Dict[str, int] = None,
        alcohol_free: Dict[str, int] = None,
        foods: Dict[str, int] = None,
    ) -> Optional[str]:
        self.orders[full_name] = {}
        if alcohol == None and foods == None and alcohol_free == None:
            return f"No order has been made"
        self.orders[full_name] = {}
        if alcohol == None:
            pass
        else:
            for key, value in alcohol.items():
                self.orders[full_name][key] = dict(
                    self.menu["drinks"]["Alcohol"][key].items()
                )
                self.orders[full_name][key]["quantity"] = value
        if alcohol_free == None:
            pass
        else:
            for key, value in alcohol_free.items():
                self.orders[full_name][key] = dict(
                    self.menu["drinks"]["Alcohol free"][key].items()
                )
                self.orders[full_name][key]["quantity"] = value
        if foods == None:
            pass
        else:
            for key in self.menu.keys():
                for item, value in foods.items():
                    if item not in self.menu[key]:
                        continue
                    else:
                        self.orders[full_name][item] = dict(
                            self.menu[key][item].items()
                        )
                        self.orders[full_name][item]["quantity"] = value

    def add_to_order(
        self,
        full_name: str,
        alcohol: Dict[str, int] = None,
        alcohol_free: Dict[str, int] = None,
        foods: Dict[str, int] = None,
    ) -> None:
        if alcohol == None:
            pass
        else:
            for key, value in alcohol.items():
                self.orders[full_name][key] = dict(
                    self.menu["drinks"]["Alcohol"][key].items()
                )
                self.orders[full_name][key]["quantity"] = value
        if alcohol_free == None:
            pass
        else:
            for key, value in alcohol_free.items():
                self.orders[full_name][key] = dict(
                    self.menu["drinks"]["Alcohol free"][key].items()
                )
                self.orders[full_name][key]["quantity"] = value
        if foods == None:
            pass
        else:
            for key in self.menu.keys():
                for item, value in foods.items():
                    if item not in self.menu[key]:
                        continue
                    else:
                        self.orders[full_name][item] = dict(
                            self.menu[key][item].items()
                        )
                        self.orders[full_name][item]["quantity"] = value

    def remove_from_order(self, full_name: str, what_to_remove: str) -> None:
        del self.orders[full_name][what_to_remove]

    def update_order_quantities(
        self,
        full_name: str,
        alcohol: Dict[str, int] = None,
        alcohol_free: Dict[str, int] = None,
        foods: Dict[str, int] = None,
    ) -> None:
        if alcohol == None:
            pass
        else:
            for key, value in alcohol.items():
                self.orders[full_name][key]["quantity"] = value
        if alcohol_free == None:
            pass
        else:
            for key, value in alcohol_free.items():
                self.orders[full_name][key]["quantity"] = value
        if foods == None:
            pass
        else:
            for key, value in foods.items():
                self.orders[full_name][key]["quantity"] = value

    def add_to_order_quantities(
        self,
        full_name: str,
        alcohol: Dict[str, int] = None,
        alcohol_free: Dict[str, int] = None,
        foods: Dict[str, int] = None,
    ):
        if alcohol == None:
            pass
        else:
            for key, value in alcohol.items():
                self.orders[full_name][key]["quantity"] += value
        if alcohol_free == None:
            pass
        else:
            for key, value in alcohol_free.items():
                self.orders[full_name][key]["quantity"] += value
        if foods == None:
            pass
        else:
            for key, value in foods.items():
                self.orders[full_name][key]["quantity"] += value

    def subtract_from_order_amounts(
        self,
        full_name: str,
        alcohol: Dict[str, int] = None,
        alcohol_free: Dict[str, int] = None,
        foods: Dict[str, int] = None,
    ):
        if alcohol == None:
            pass
        else:
            for key, value in alcohol.items():
                amount = self.orders[full_name][key]["quantity"]
                self.orders[full_name][key]["quantity"] = amount - value
                if self.orders[full_name][key]["quantity"] == 0:
                    del self.orders[full_name][key]
        if alcohol_free == None:
            pass
        else:
            for key, value in alcohol_free.items():
                amount = self.orders[full_name][key]["quantity"]
                self.orders[full_name][key]["quantity"] = amount - value
                if self.orders[full_name][key]["quantity"] == 0:
                    del self.orders[full_name][key]
        if foods == None:
            pass
        else:
            for key, value in foods.items():
                amount = self.orders[full_name][key]["quantity"]
                self.orders[full_name][key]["quantity"] = amount - value
                if self.orders[full_name][key]["quantity"] == 0:
                    del self.orders[full_name][key]

    def show_order_summarized(self, full_name: str) -> None:
        total_cost = self.show_order_cost(full_name=full_name)
        ordered_things = {}
        for key, value in self.orders[full_name].items():
            for inner_key, inner_value in self.orders[full_name][key].items():
                if inner_key == "quantity":
                    ordered_things[key] = inner_value
                else:
                    continue
        print(f"Total cost is: {total_cost}")
        print("Your order is:")
        for key, value in ordered_things.items():
            print(f"{key}, amount: {value}")

    def show_order_cost(self, full_name: str) -> None:
        cost = 0
        for key in self.orders[full_name].keys():
            quantity = self.orders[full_name][key]["quantity"]
            cost = cost + (self.orders[full_name][key]["price"] * quantity)
        return cost