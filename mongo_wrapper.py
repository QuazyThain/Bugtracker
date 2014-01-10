# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 16:19:06 2014

@author: quazythain
"""

from pymongo import MongoClient


class MongoModel(object):
    def __init__(self, db="mongomodel"):
        self.db_name = db

    def connect(self):

        try:
            connection = MongoClient(host="mongodb://localhost", port=27017)
            db = connection[self.db_name]
            return db
        except:
            return "Can't connect to database"

    def collection_switch(self, collection=None):

        try:
            return self.connect()[collection]
        except:
            return "Can't switch on collection"

    def insert(self, collection, document):
        collection = self.collection_switch(collection)

        try:
            collection.insert(document, safe=True)
        except:
            return "Can't add data to collection"

    def select(self, collection):
        collection = self.collection_switch(collection)

        try:
            collection.find().pretty()
        except:
            return "Can't select data from collection"

if __name__ == "__main__":
    mm = MongoModel()
    mm.connect()
    mm.collection_switch("users")
    mm.select("users")
