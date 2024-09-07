#!/usr/bin/python3

import pymongo
 
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

#list all databases
dblist = myclient.list_database_names()
for db in dblist:
    print(db)

#list all collections
mydb = myclient["mydb"]
colist = mydb.list_collection_names()
for col in colist:
    print(col)

mycol = mydb['mycol']
#find all records in collection
rs = mycol.find()
for r in rs:
    print(r)

mydict = { "name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com" }

result = mycol.insert_one(mydict)
print(result)

 
mylist = [
  { "name": "Taobao", "alexa": "100", "url": "https://www.taobao.com" },
  { "name": "QQ", "alexa": "101", "url": "https://www.qq.com" },
  { "name": "Facebook", "alexa": "10", "url": "https://www.facebook.com" },
  { "name": "知乎", "alexa": "103", "url": "https://www.zhihu.com" },
  { "name": "Github", "alexa": "109", "url": "https://www.github.com" }
]
result = mycol.insert_many(mylist)
print(result)

#drop all records in collection
result = mycol.delete_many({"name":"RUNOOB"})
print(result.deleted_count)
#drop a collection
# mycol.drop()
# If filter is empty, all records will be deleted
# mycol.delete_many({})