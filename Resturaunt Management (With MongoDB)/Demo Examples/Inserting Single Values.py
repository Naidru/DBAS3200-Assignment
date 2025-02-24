# Insert a document and retrieve the auto-generated _id.

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["my_database"]
collection = db["my_collection"]

# Define a document
document = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Insert the document and get the generated ID
result = collection.insert_one(document)
print("Inserted document ID:", result.inserted_id)

# Info: MongoDB generates `_id` as an `ObjectId` (a unique 12-byte identifier).