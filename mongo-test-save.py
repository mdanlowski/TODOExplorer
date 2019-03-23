#mongo-test
import pymongo
import json
# collection (table)
# document (record) before it actually creates the database (and collection)

# todos_coll.delete_many({}) ## -> purges column
# todos_coll.find({_id: 1}) ## -> finds item by key

DBHANDLER = pymongo.MongoClient("mongodb://localhost:27017/")
working_db = DBHANDLER["todoExpl"]
db_up_list = DBHANDLER.list_database_names()
todos_coll = working_db["todos"]
todos_source = open('results_2019-03-22_14-31-02.json', 'r')
todos = json.load(todos_source)

_id_ = 1
todos_arr = []
for k in todos.keys():
    todos[k]["_id"] = _id_
    _id_ += 1
    todos_arr.append(todos[k])

array_here = todos_arr


# To insert a record, or document as it is called in MongoDB, into a COLLECTION (table), we use the insert_one() method.
# dict_here = { "name": "John", "address": "Highway 37" }
# x = todos_coll.insert_one(dict_here) # TO INSERT ONE DOCUMENT (record)
x = todos_coll.insert_many(array_here) # TO INSERT MANY DOCUMENTS (records)

# xid = x.inserted_id # last item's ID
# print(xid)

# COLLECTIONS (good'ol tables) in database
coll_list = working_db.list_collection_names()

print( "todoExpl" in db_up_list, '\n', coll_list )
