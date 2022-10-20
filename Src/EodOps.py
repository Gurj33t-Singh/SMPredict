from MongoConnect import *
import GetConfigs
import pymongo
from ParseFile import *


class Eod:
    TrainDataList=None

    def getTrainData(self):
        TrainData = ReadFile("TrainFilePath", "rt")
        TrainData.jsonFileToDict()
        TrainData.getDataList()
        self.TrainDataList=TrainData.DataList

    def CreateTrainCollection(self):
        self.getTrainData()
        LocalMongo = MongoCon(GetConfigs.getConf("MongoURL"), GetConfigs.getConf("DB"),
                              GetConfigs.getConf("TrainingCollection"))
        LocalMongo.Collection.create_index([(GetConfigs.getConf("UniqueKey"), pymongo.ASCENDING)], unique=True)
        LocalMongo.Collection.insert_many(self.TrainDataList)
        for doc in LocalMongo.Collection.find():
            print(doc)
