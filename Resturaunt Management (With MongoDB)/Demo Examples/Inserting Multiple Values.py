# Insert multiple documents and retrieve their generated _ids.

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["my_database"]
collection = db["my_collection"]

# Define multiple documents
documents = [
    {"name": "Bob", "age": 30, "city": "Los Angeles"},
    {"name": "Charlie", "age": 28, "city": "Chicago"},
    {"name": "David", "age": 35, "city": "San Francisco"}
]

# Insert multiple documents and get their generated IDs
result = collection.insert_many(documents)
print("Inserted document IDs:", result.inserted_ids)