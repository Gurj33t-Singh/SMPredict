from MongoConnect import *
import GetConfigs
import pymongo
from ParseFile import *


class Eod:
    DataList=None
    FilePathConf=None
    FileModeStr=None
    MongoUrlConf=None
    DBConf=None
    CollectionConf=None
    UniqueKeyConf=None

    #initialise variables
    def __init__(self, FilePathConf, FileModeStr, MongoUrlConf, DBConf, CollectionConf,
                 UniqueKeyConf):
        self.FilePathConf=FilePathConf
        self.FileModeStr=FileModeStr
        self.MongoUrlConf=MongoUrlConf
        self.DBConf=DBConf
        self.CollectionConf=CollectionConf
        self.UniqueKeyConf=UniqueKeyConf

    def getJsonData(self):
        TrainData = ReadFile(self.FilePathConf, self.FileModeStr)
        TrainData.jsonFileToDict()
        self.getDataList(TrainData.Dict)

    def CreateTrainCollection(self):
        self.getJsonData()
        LocalMongo = MongoCon(GetConfigs.getConf(self.MongoUrlConf), GetConfigs.getConf(self.DBConf),
                              GetConfigs.getConf(self.CollectionConf))
        LocalMongo.Collection.create_index([(GetConfigs.getConf(self.UniqueKeyConf), pymongo.ASCENDING)], unique=True)
        LocalMongo.Collection.insert_many(self.DataList)
        for doc in LocalMongo.Collection.find():
            print(doc)

    # Get stock data from dictionary as list
    def getDataList(self, eodDict):
        for index in eodDict:
            if (index == "data"):
                self.DataList = eodDict[index]
