from ParseFile import ReadJson
import pymongo

class MongoCon:
    Client = None
    db = None
    Collection = None
    #insertTrainList = trainCollection.insert_many(TrainData.DataList)
    def ClientCon(self, MongoUrl):
        self.Client=pymongo.MongoClient(MongoUrl)

    def DbCon(self, DbNameStr):
        self.db=self.Client[DbNameStr]

    def CollectionCon(self, CollectionNameStr):
        self.Collection=self.db[CollectionNameStr]

