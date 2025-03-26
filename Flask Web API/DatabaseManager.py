from pymongo import MongoClient
from bson import ObjectId

class DatabaseManager:
    def __init__(self):
        """
        Initialize the database connection and get the tasks collection.
        """
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["taskmanager"]
        self.tasks_collection = self.db["tasks"]
        self.counter_collection = self.db["counters"]
        self.current_id = self._initialize_id_counter()

    def _initialize_id_counter(self):
        """
        Initialize the ID counter from the database.
        :return: The current ID counter value.
        """
        counter = self.counter_collection.find_one({"_id": "task_id"})
        if counter is None:
            self.counter_collection.insert_one({"_id": "task_id", "value": 0})
            return 0
        return counter["value"]

    def _increment_id_counter(self):
        """
        Increment the ID counter in the database.
        :return: The new ID counter value.
        """
        result = self.counter_collection.find_one_and_update(
            {"_id": "task_id"},
            {"$inc": {"value": 1}},
            return_document=True
        )
        return result["value"]

    def check_task_exists(self, task_id):
        """
        Check if a task with the given title exists in the database.
        :param task_id:
        :return:
        """
        query = {"task_id": task_id}
        return self.tasks_collection.find_one(query)

    def get_all_task(self):
        """
        Get all tasks from the database.
        :return:
        """
        tasks = self.tasks_collection.find()
        return list(tasks)

    def add_task(self, task):
        """
        Add a new task to the database.
        :param task:
        :return:
        """
        task["task_id"] = self._increment_id_counter()
        self.tasks_collection.insert_one(task)

    def delete_task(self, task_title):
        """
        Delete a task from the database.
        :param task_title:
        :return:
        """
        query = {"title": task_title.lower()}
        result = self.tasks_collection.delete_one(query)
        return result.deleted_count

    def update_task(self, task_id, update_data):
        """
        Update an existing task in the database.
        :param task_id:
        :param update_data:
        :return:
        """
        query = {"task_id": task_id}
        update = {"$set": update_data}
        result = self.tasks_collection.update_one(query, update)
        return result.modified_count

def convert_to_json_serializable(doc):
    if isinstance(doc, list):
        return [convert_to_json_serializable(d) for d in doc]
    if isinstance(doc, dict):
        return {k: convert_to_json_serializable(v) for k, v in doc.items()}
    if isinstance(doc, ObjectId):
        return str(doc)
    return doc