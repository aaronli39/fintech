import pymongo
from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://student:PqyqrY2aEC22B5SB@cluster0-ya1yr.mongodb.net/stock-prices?retryWrites=true")
# Make sure to replace this with the name of the database!
db = client["stock-prices"]
collection = db.prices

# write your queries here
print("everything")
print(list(collection.find({})))

print("microsoft stuff")
for i in collection.find({"symbol": "MSFT"}):
    print(i)

print("2004 stocks")
for i in collection.find({"year": 2004}):
    print(i)

print("september stocks")
for i in collection.find({"month": "Sep"}):
    print(i)

print("september 2004")
for i in collection.find({"month": "Sep", "year": 2004}):
    print(i)

print("stock prices lowest to highest")
temp = list(collection.find({}).sort("price", pymongo.ASCENDING))

vals = [temp[i]["price"] for i in range(len(temp))]
print(vals)

print("stock prices highest to lowest")
temp = list(collection.find({}).sort("price", pymongo.DESCENDING))
vals = [temp[i]["price"] for i in range(len(temp))]
print(vals)

print("first 5")
temp = list(collection.find({}))
for i in range(5):
    print(temp[i])
