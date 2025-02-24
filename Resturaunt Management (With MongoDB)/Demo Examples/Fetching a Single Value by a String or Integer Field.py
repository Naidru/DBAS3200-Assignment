# Retrieve a document by a known field (like name), handling cases with no matches or multiple matches.

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["my_database"]
collection = db["my_collection"]

# Search for a user by name
query = {"name": "Alice"}
documents = list(collection.find(query))

# Verify number of returned documents
if len(documents) == 0:
    print("No document found with that name.")
elif len(documents) == 1:
    print("Found document:", documents[0])
else:
    print(f"Multiple documents found ({len(documents)}). First result:", documents[0])