import pymongo

conn_str = "mongodb+srv://ben:ben@cluster0.zeumy.mongodb.net/maindb?retryWrites=true&w=majority"

# set a 5-second connection timeout
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)

try:
    print(client.server_info())
except Exception:
    print("Unable to connect to the server.")
