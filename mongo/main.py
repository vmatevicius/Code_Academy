from typing import List, Dict
from pymongo import MongoClient
from pymongo.collection import Collection

client = MongoClient("mongodb://localhost:27017/")
db = client["grocery_store"]


def get_items_sorted_by_date(collection_name: Collection, date: str) -> List:
    collection = db[collection_name]
    query = {"year made": {"$eq": date}}
    return list(collection.find(query))


def calculate_monetary_value(items: List) -> float:
    total_value = 0
    for item in items:
        total_value += item["price"]
    return total_value


def get_all_items_prices(collection_name: Collection) -> List:
    collection = db[collection_name]
    return list(collection.find({}, {"price": 1}))


def calculate_average_price(prices: List) -> float:
    total_sum = 0
    for price in prices:
        total_sum += price["price"]
    return round(total_sum / len(prices), 2)


def filter_items_by_price_range(
    collection_name: Collection,
    value_one: float,
    operator_one: str,
    value_two: float,
    operator_two: str,
) -> List:
    collection = db[collection_name]
    query = {"price": {operator_one: value_one, operator_two: value_two}}
    return list(collection.find(query))


def filter_items_by_first_name_letter(items: List, letter: str) -> List:
    filtered_items = []
    for item in items:
        if item["name"].startswith(letter):
            filtered_items.append(item)
        else:
            continue
    return filtered_items


def find_items_by_price(collection_name: str, value: int, operator: str) -> List:
    collection = db[collection_name]
    query = {"price": {operator: value}}
    return list(collection.find(query))


def find_items_by_quantity(collection_name: str, value: int, operator: str) -> List:
    collection = db[collection_name]
    query = {"quantity": {operator: value}}
    return list(collection.find(query))


def count_all_names_from_dict(dictionary: Dict) -> Dict[str, int]:
    names = {}
    for item in dictionary:
        if item["name"] not in names.keys():
            names.update({item["name"]: 0})
        else:
            names[item["name"]] += 1
    return names


COLLECTIONS = ["electronics", "food", "pets"]

# Find all item names (only) for prices > 50 and quantity < 10.

for collection_name in COLLECTIONS:
    by_price = find_items_by_price(
        collection_name=collection_name, value=50, operator="$gt"
    )
    by_quantity = find_items_by_quantity(
        collection_name=collection_name, value=10, operator="$lt"
    )
    all_items = by_price + by_quantity

print(count_all_names_from_dict(all_items))

# Get all items which names starts with letter a, and cost is between 10 and 100.

items = filter_items_by_price_range(
    collection_name="food",
    value_one=100,
    operator_one="$lt",
    value_two=10,
    operator_two="$gt",
)
print(filter_items_by_first_name_letter(items=items, letter="a"))

# Get average price for all items/categories in the store.
all_items_prices = []
average_prices = {}
for collection_name in COLLECTIONS:
    items = get_all_items_prices(collection_name=collection_name)
    average_prices[collection_name] = calculate_average_price(items)
    all_items_prices = items + all_items_prices

print(f" average prices of each categorie {average_prices}")
print(f" average price of all items: {calculate_average_price(all_items_prices)}")

# Get all electronic items monetary value made 1 years, 2 months and 12 days from today.

items = get_items_sorted_by_date(collection_name="electronics", date="2022-03-12")
print(f" monetary value : {calculate_monetary_value(items)}")
