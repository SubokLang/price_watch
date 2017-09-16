import pymongo

class Database():
    URI = "mongodb://127.0.0.1:27017"
    DB = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DB = client['fullstack']
        #print(Database.DB)

    @staticmethod
    def insert(collection, data):
        #print(collection)
        #print(Database.DATABASE)
        #print(data)
        Database.DB[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DB[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        #print(collection)
        #print(Database.DB)
        #print(query)
        #print(type(query))
        return Database.DB[collection].find_one(query)