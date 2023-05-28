from typing import Dict

# # Task Nr.4:

# # Create three different task with real world scenario what would include all magic methods we covered today and plus 3 others from the provided list.


# class Cow:
#     def __init__(self, weight: float, age: int, name: str = None) -> None:
#         self.age = age
#         self.weight = weight
#         self.name = name

#     def __str__(self) -> str:
#         return f"Moooo"

#     def __repr__(self) -> str:
#         return f"Cow age = {self.age}, weight = {self.weight}, name = {self.name}"

#     def __bool__(self) -> bool:
#         if self.name != None:
#             return True
#         return False

#     def __call__(self) -> str:
#         return f"you summoned a cow"

#     def __lt__(self, other_cow_object) -> bool:
#         if self.weight < other_cow_object.weight:
#             return True

#     def __gt__(self, other_cow_object) -> bool:
#         if self.weight > other_cow_object.weight:
#             return True


# cow = Cow(weight=200, age=10)
# cow_two = Cow(weight=300, age=11, name="Artiomas")
# print(cow())
# print(cow)
# print(bool(cow))
# print(repr(cow))
# if bool(cow):
#     print(f"This cows name is {cow.name}")
# else:
#     print("This cow does not have a name")
# if cow > cow_two:
#     print("first cow is heavier")
# else:
#     print("second cow is heavier")


class ShoppingCart:
    def __init__(self, owners_name: str) -> None:
        self.owners_name: str = owners_name
        self.inventory: Dict[int, str] = {}

    def add_item(self, item: str, quantity: int) -> None:
        self.inventory[item] = quantity

    def __str__(self) -> str:
        return "This is your shopping cart"

    def __bool__(self) -> bool:
        if len(self.inventory) == 0:
            return False
        return True

    # def __add__(self, other_cart: "ShoppingCart") -> "ShoppingCart":
    #     return ShoppingCart(
    #         list(self.inventory.items()) + list(other_cart.inventory.items())
    #     )

    def __lt__(self, other_cart: "ShoppingCart") -> bool:
        if self.inventory < other_cart.inventory:
            return True

    def __gt__(self, other_cart: "ShoppingCart") -> bool:
        if self.inventory > other_cart.inventory:
            return True

    def __len__(self):
        return len(list(self.inventory.keys()))


cart = ShoppingCart(owners_name="Antanas")
other_cart = ShoppingCart(owners_name="Nezinosi")
cart.add_item(item="Alus", quantity=2)
cart.add_item(item="Duona", quantity=1)
other_cart.add_item(item="Batonas", quantity=3)

print(cart.inventory)
print(other_cart.inventory)
print(len(cart))
print(len(other_cart))

if len(cart) > len(other_cart):
    print("First cart has more items")
else:
    print("Second cart has more items")

# super_cart = cart + other_cart
# print(super_cart.inventory)
