import pymongo

client = pymongo.MongoClient("mongodb+srv://sridher:sridher1@cluster0.vx0qyeu.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d1 ={
    "name":"Sridher1",
    "email": "sridhar@gmail.com",
    "suname": "siripuram1"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d1)