from pymongo import MongoClient
from typing import Dict, Any, List, Optional

task_one = {
    "task_name": "mop floors",
    "age_required": 10,
    "description": "I must see my reflection on the foor",
    "deadline": "2023-05-23",
    "employees_included": ["Antanas", "Antano brolis"],
    "status": "in progress",
    "task_difficulty": "beginner level",
    "reward": "loaf of bread",
    "exp_points": 123,
}


class TaskManager:
    def __init__(
        self, host: str, port: int, db_name: str, collection_name: str
    ) -> None:
        self.client = MongoClient(host, port)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def create_task(self, task: Dict[str, Any]) -> str:
        result = self.collection.insert_one(task)
        return str(result.inserted_id)

    def get_all_tasks(self) -> List[Dict[str, Any]]:
        return list(self.collection.find())

    def get_task(self, task_name: str) -> Dict[str, Any]:
        return list(self.collection.find({"task_name": task_name}))

    def update_task(self, task_name: str, task_updates: Dict[str, Any]) -> bool:
        result = self.collection.update_one(
            {"task_name": task_name}, {"$set": task_updates}
        )
        return result.modified_count > 0

    def delete_task(self, task_name: str) -> bool:
        result = self.collection.delete_one({"task_name": task_name})
        return result.deleted_count > 0

    def get_single_querry(
        self, querry: Dict[str, Any], fields: Dict[str, Any]
    ) -> Optional[Dict[str, Any]]:
        return self.collection.find_one(querry, fields)


task_manager = TaskManager(
    host="localhost", port=27017, db_name="Tasksdb", collection_name="beginner tasks"
)

# print(task_manager.create_task(task_one))

query = {"age_required": 18}
fields = {"description": 0, "exp_points": 0}

document = task_manager.get_single_querry(query, fields)
print(document)
