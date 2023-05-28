from typing import List, Dict
from pymongo import MongoClient
from pymongo.collection import Collection

client = MongoClient("mongodb://localhost:27017/")
db = client["grocery_store"]

# Get all electronic items monetary value made 1 years, 2 months and 12 days from today.


def get_items_sorted_by_date(collection_name: Collection, date: str) -> List:
    collection = db[collection_name]
    query = {"year made": {"$eq": date}}
    return list(collection.find(query))


def calculate_monetary_value(items: List) -> float:
    total_value = 0
    for item in items:
        total_value += item["price"]
    return total_value


items = get_items_sorted_by_date(collection_name="electronics", date="2022-03-12")
print(f" monetary value : {calculate_monetary_value(items)}")

# Get average price for all items/categories in the store.


def get_all_items_prices(collection_name: Collection) -> List:
    collection = db[collection_name]
    return list(collection.find({}, {"price": 1}))


def calculate_average_price(prices: List) -> float:
    total_sum = 0
    for price in prices:
        total_sum += price["price"]
    return round(total_sum / len(prices), 2)


electronics = get_all_items_prices(collection_name="electronics")
food = get_all_items_prices(collection_name="food")
pets = get_all_items_prices(collection_name="pets")
all_items = electronics + food + pets
print(f" average electronic item price: {calculate_average_price(electronics)}")
print(f" average food item price: {calculate_average_price(food)}")
print(f" average pet price: {calculate_average_price(pets)}")
print(f" average price of all items: {calculate_average_price(all_items)}")


# Get all items which names starts with letter a, and cost is between 10 and 100.
def filter_items_by_price_range(
    collection_name: Collection, value_one: float, value_two: float
) -> List:
    collection = db[collection_name]
    query = {"price": {"$lt": value_one, "$gt": value_two}}
    return list(collection.find(query))


def filter_items_by_first_name_letter(items: List, letter: str) -> List:
    filtered_items = []
    for item in items:
        if item["name"].startswith(letter):
            filtered_items.append(item)
        else:
            continue
    return filtered_items


items = filter_items_by_price_range(collection_name="food", value_one=100, value_two=10)
print(filter_items_by_first_name_letter(items=items, letter="a"))


# Find all item names (only) for prices > 50 and quantity < 10.

collection = db["electronics"]
query = {
    "price": {"$gt": 50},
    "quantity": {"$lt": 10},
}
electronics_items = list(collection.find(query))
collection = db["food"]
food_items = list(collection.find(query))
collection = db["pets"]
pets = list(collection.find(query))
all_items = electronics_items + food_items + pets
