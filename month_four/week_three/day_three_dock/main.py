# Google is launching a network of autonomous pizza delivery drones
# and wants you to create a flexible rewards system (Pizza Points™)
# that can be tweaked in the future.
# The rules are simple: if a customer has made at least N orders of at least Y price,
# they get a FREE pizza! Create a function that takes a dictionary of customers,
# a minimum number of orders and a minimum order price. Return a list of customers that are eligible for a free pizza.


class PizzaRestaurant:
    def __init__(self):
        self.customers = []
        self.orders = []

    def add_customer(self, customer: "Customer") -> None:
        new_customer = {
            "id": ...,
            "name": customer.name,
            "surname": customer.surname,
            "points": customer.pizza_points,
        }
        self.customers.append(new_customer)
        return new_customer

    def make_order(self, name: str, surname: str, price: float) -> None:
        pass

    def is_eligible_for_free_pizza(self) -> bool:
        pass

    def is_eligible_for_pizza_point(self) -> bool:
        pass

    def get_new_id(self) -> int:
        id_list = []
        if self.customers != []:
            for customer in self.customers:
                id_list.append(customer.id)
        else:
            print("poop")

        # get highest id number and  add +1 to it


class Customer:
    def __init__(self, name: str, surname: str) -> None:
        self.id = 0
        self.name = name
        self.surname = surname
        self.pizza_points = 0


class Order:
    def __init__(self, name: str, surname: str, price: float) -> None:
        self.name = name
        self.surname = surname
        self.price = price
