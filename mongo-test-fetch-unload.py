#mongo-test
import pymongo
import json
# collection (table)
# document (record) before it actually creates the database (and collection)

DBHANDLER = pymongo.MongoClient("mongodb://localhost:27017/")
working_db = DBHANDLER["todoExpl"]
collections = working_db.list_collection_names()
todos_coll = working_db["todos"]

for todo in todos_coll.find():
	print(todo)


# To insert a record, or document as it is called in MongoDB, into a COLLECTION (table), we use the insert_one() method.
# dict_here = { "name": "John", "address": "Highway 37" }
# x = todos_coll.insert_one(dict_here) # TO INSERT ONE DOCUMENT (record)

