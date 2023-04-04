from typing import List, Dict

# from datetime import datetime

# print(datetime.now().strftime("%H"))


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


orders = Orders()
orders.make_order(
    name="Antanas",
    surname="Barabanas",
    foods={
        "Fish": 2,
    },
)
for order in orders.orders:
    print(order.foods)
