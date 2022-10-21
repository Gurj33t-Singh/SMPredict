from FileOps import Fops
import pymongo

class MongoCon:

    """Client = None
    db = None"""

    Collection = None


    def __init__(self, mongoUrlStr, dbNameStr, collectionNameStr):
        """self.ClientCon(mongoUrlStr)
        self.DbCon(dbNameStr)
        self.CollectionCon(collectionNameStr)"""
        self.Collection=pymongo.MongoClient(mongoUrlStr)[dbNameStr][collectionNameStr]

    """
    def ClientCon(self, MongoUrlStr):
        self.Client=pymongo.MongoClient(MongoUrlStr)

    def DbCon(self, DbNameStr):
        self.db=self.Client[DbNameStr]

    def CollectionCon(self, CollectionNameStr):
        self.Collection=self.db[CollectionNameStr]
        """

