# Use query operators to retrieve multiple documents.

# $in: Matches any value in a given list.
# $gt: Greater than (>)
# $lt: Less than (<)

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["my_database"]
collection = db["my_collection"]

# Fetch all users whose names are in a given list
query_in = {"name": {"$in": ["Alice", "Bob"]}}
results_in = list(collection.find(query_in))

print(f"Users with matching names ({len(results_in)} found):")
for doc in results_in:
    print(doc)

# Fetch users older than 25
query_gt = {"age": {"$gt": 25}}
results_gt = list(collection.find(query_gt))

print(f"\nUsers older than 25 ({len(results_gt)} found):")
for doc in results_gt:
    print(doc)