from ParseFile import ReadFile
import pymongo

class MongoCon:
    Client = None
    db = None
    Collection = None
    #insertTrainList = trainCollection.insert_many(TrainData.DataList)

    def __init__(self, mongoUrlStr, dbNameStr, collectionNameStr):
        self.ClientCon(mongoUrlStr)
        self.DbCon(dbNameStr)
        self.CollectionCon(collectionNameStr)

    def ClientCon(self, MongoUrlStr):
        self.Client=pymongo.MongoClient(MongoUrlStr)

    def DbCon(self, DbNameStr):
        self.db=self.Client[DbNameStr]

    def CollectionCon(self, CollectionNameStr):
        self.Collection=self.db[CollectionNameStr]

