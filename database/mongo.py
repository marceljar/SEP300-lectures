from pymongo import MongoClient, ASCENDING, DESCENDING
from credentials import ATLAS_URI, DB_NAME, COLL_NAME

with MongoClient(ATLAS_URI) as client:
    db = client[DB_NAME]
    coll = db[COLL_NAME]

    print("\nAll users:")
    for doc in coll.find().sort("user_id", ASCENDING):
        print(doc["user_id"], doc["first_name"], \
              doc["last_name"], doc["balance"])

    doc = coll.find_one({"user_id": 1})
    if doc is None:
        print("No user with id 1")
    else:
        print("\nInfo about first user:")
        print(f"{doc['user_id']} {doc['first_name']} \
              {doc['last_name']} {doc['balance']}")

    print("\nUsers with balance >= 100")
    for doc in coll.find({"balance": {"$gte": 100.00}})\
                   .sort("balance", DESCENDING):
        print(doc["first_name"], doc["last_name"], \
              doc["balance"])

    coll.update_one({"user_id": 1}, \
                    {"$inc": {"balance": 10.00}})
    coll.update_one({"user_id": 2}, \
                    {"$set": {"last_name": "Thompson"}})

    print("\nAfter updates (Alice, Bob):")
    for doc in coll.find({"user_id": \
                {"$in": [1, 2]}}).sort("user_id", ASCENDING):
        print(doc["user_id"], doc["first_name"],\
              doc["last_name"], doc["balance"])

    coll.delete_one({"user_id": 12})
    coll.delete_many({"balance": {"$lt": 10.00}})

    print("\nRemaining users:")
    for doc in coll.find().sort("user_id", ASCENDING):
        print(doc["user_id"], doc["first_name"], \
              doc["last_name"], doc["balance"])
