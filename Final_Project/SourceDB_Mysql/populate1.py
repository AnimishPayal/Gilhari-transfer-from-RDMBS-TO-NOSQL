from pymongo import MongoClient
import json

# Function to load JSON data from a file
def load_json_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# MongoDB connection configuration
def connect_to_mongodb(uri, db_name):
    client = MongoClient(uri)
    return client[Destination_DB]

def main():
    # Configuration
    mongo_uri = 'mongodb://localhost:27017/'  # Replace with your MongoDB URI
    db_name = 'Destination_DB'  # Replace with your database name
    collection_name = 'Allotted_LIST'  # Replace with your collection name
    json_file_path = 'data.json'  # Replace with your JSON file path

    # Load JSON data
    json_data = load_json_data(json_file_path)

    # Connect to MongoDB and get the collection
    db = connect_to_mongodb(mongo_uri, db_name)
    collection = db[collection_name]

    # Insert JSON data into the collection
    if isinstance(json_data, list):  # Check if the data is a list of documents
        result = collection.insert_many(json_data)
        print(f"Inserted document IDs: {result.inserted_ids}")
    else:
        print("The JSON data should be a list of documents.")

if __name__ == "__main__":
    main()
