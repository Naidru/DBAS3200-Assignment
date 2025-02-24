# Fetch a document first, then update it using _id.

from pymongo import MongoClient
from bson import ObjectId  # Needed for working with MongoDB ObjectIds

client = MongoClient("mongodb://localhost:27017/")
db = client["my_database"]
collection = db["my_collection"]

# Find a document by name
query = {"name": "Alice"}
documents = list(collection.find(query))

if len(documents) == 0:
    print("No document found to update.")
elif len(documents) == 1:
    doc_id = documents[0]["_id"]  # Get the _id
    update = {"$set": {"age": 26}}  # Modify the age
    result = collection.update_one({"_id": doc_id}, update)
    print("Updated documents:", result.modified_count)
else:
    print(f"Multiple documents found ({len(documents)}). Skipping update to avoid conflicts.")