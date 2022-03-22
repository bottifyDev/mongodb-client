from pymongo import MongoClient
from pymongo import *
client = MongoClient("mongodb+srv://ben:ben@cluster0.zeumy.mongodb.net/maindb?retryWrites=true&w=majority")

db = client['maindb']
