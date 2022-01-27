import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

db = myclient["mine"]
ct1  = db.collection_1
ct1.insert_one({'one': 1})
print(myclient.list_database_names())