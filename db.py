from pymongo import MongoClient


class Connection:

    def get_connection():
        client = MongoClient(
                            host="localhost",
                            port=27017,
                            username="admin",
                            password="secretpass",
                            authSource="admin")
        db = client["threat_db"]
        return db
    
    def insert_to_db(data):
        db = Connection.get_connection()
        information = db["top_threats"]
        result = information.insert_many(data)
        return result
    
# class DBConnection:
#     @staticmethod
#     def get_connection():
#         client = MongoClient("mongodb+srv://<###myname###>:HxDGLWDvLaLvgJBV@cluster0.a8kyzcd.mongodb.net/")
#         db = client["threats"]
#         collection = db["top_threats"]
#         return collection


# class DBCrud:
#     _collection = DBConnection.get_connection()

#     @staticmethod
#     def insert_data(top: list[dict]):
#         DBCrud._collection.insert_many(top)
#         print("Data inserted.")
