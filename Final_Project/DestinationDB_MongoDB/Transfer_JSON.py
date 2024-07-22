import json
from pymongo import MongoClient

# Replace with your MongoDB connection string
mongo_uri = "mongodb://localhost:27017"

# Connect to the MongoDB server
client = MongoClient(mongo_uri)  # This uses the native MongoDB API to connect

# Replace 'your_database' with the name of your database
db = client.db2  # Access the database

# Replace 'your_collection' with the name of your collection
collection = db.db2  # Access the collection

# Load JSON data from file
with open('Allotted_LIST.json') as file:
    json_data = json.load(file)

# Insert JSON data into the collection using native API methods
if isinstance(json_data, list):
    collection.insert_many(json_data)  # Use the native API method to insert multiple documents
else:
    collection.insert_one(json_data)  # Use the native API method to insert a single document

print("Data inserted successfully!")

# Close the MongoDB connection
client.close()  # Close the connection using the native API method
