from classes import Reservation, Order
from typing import Union, Dict, Optional


class Cafeteria:
    def __init__(self) -> None:
        pass

    def add_tips(self, tip_percentage: int, order_cost: float = None) -> float:
        return order_cost + (order_cost / 100 * tip_percentage)


hmmm = Order()
hmmm.make_order(
    full_name="Vadimas",
    alcohol={"Beer": 2, "Vine": 1},
    alcohol_free={"Orange juice": 1},
    foods={"Steak": 2, "Fish": 1},
)
hmmm.add_to_order_quantities(full_name="Vadimas", alcohol={"Beer": 1, "Vine": 1})
hmmm.subtract_from_order_amounts(full_name="Vadimas", alcohol={"Beer": 3, "Vine": 2})
hmmm.add_to_order(full_name="Vadimas", foods={"Grilled chicken": 2})
hmmm.remove_from_order(full_name="Vadimas", what_to_remove="Orange juice")
hmmm.show_order_summarized(full_name="Vadimas")
print(hmmm.show_order_cost(full_name="Vadimas"))

print()

hmmmm = Reservation()
print(hmmmm.show_free_tables())
hmmmm.assign_table(
    table_type="single", full_name="Vadimas Nepaimsi", reservation_time=12
)
print(hmmmm.show_free_tables())
print(hmmmm.check_reservation(full_name="Vadimas Nepaimsi"))
print(hmmmm.show_reservation(full_name="Vadimas Nepaimsi"))
print(hmmmm.show_reserved_tables())
