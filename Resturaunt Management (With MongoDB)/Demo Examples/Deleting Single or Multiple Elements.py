# Remove documents either by _id or another field.

# delete_one(query): Deletes only the first match (if found).
# delete_many(query): Deletes all matches (only if at least one match exists).

from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb://localhost:27017/")
db = client["my_database"]
collection = db["my_collection"]

# Delete a single document by name
query_single = {"name": "Alice"}
results_single = list(collection.find(query_single))

if len(results_single) == 0:
    print("No document found to delete.")
elif len(results_single) == 1:
    doc_id = results_single[0]["_id"]
    result = collection.delete_one({"_id": doc_id})
    print("Deleted single document count:", result.deleted_count)
else:
    print(f"Multiple documents found ({len(results_single)}). Skipping delete to avoid unintended removal.")

# Delete all documents where age is greater than 30
query_multiple = {"age": {"$gt": 30}}
results_multiple = list(collection.find(query_multiple))

if len(results_multiple) > 0:
    result_multiple = collection.delete_many(query_multiple)
    print("Deleted multiple documents count:", result_multiple.deleted_count)
else:
    print("No documents matched for bulk deletion.")
