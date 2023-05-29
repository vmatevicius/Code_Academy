from pymongo import MongoClient
from pymongo.collection import Collection
from typing import Dict, Any, List
from bson.objectid import ObjectId


class LibraryManager:
    def __init__(self, host: str, port: int, db_name: str, collection_name: str):
        self.client = MongoClient(host, port)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def add_book(self, book: Dict[str, Any]) -> str:
        result = self.collection.insert_one(book)
        return str(result.inserted_id)

    def get_all_books(self) -> List[Dict[str, Any]]:
        return list(self.collection.find())

    def get_book(self, book_id: str) -> Dict[str, Any]:
        return self.collection.find({"_id": ObjectId(book_id)})

    def update_book(self, book_id: str, updates: Dict[str, Any]) -> bool:
        result = self.collection.update_one({"_id": book_id}, {"$set": updates})
        return result.modified_count > 0

    def delete_book(self, book_id: str) -> bool:
        result = self.collection.delete_one({"_id": book_id})
        return result.deleted_count > 0


library = LibraryManager(
    host="localhost", port=27017, db_name="random_bullshit", collection_name="shit"
)
library.add_book(book={"name": "antanas"})
# library.update_book(
#     book_id="645d2110377a6cab2328a025", updates={"name": "atomic nonsense"}
# )
print(library.get_book(book_id="645d264609a0e3abaaff58db"))
# unknown_variable = library.delete_book(book_id="645d20e891d20e5b7f137212")
# print(unknown_variable)
