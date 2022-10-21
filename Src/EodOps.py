from MongoConnect import *
import GetConfigs
import pymongo
from FileOps import *


class Eod:
    DataList=None
    FilePathConf=None
    FileModeStr=None
    MongoUrlConf=None
    DBConf=None
    CollectionConf=None
    UniqueKeyConf=None
    DbClient=None
    DataListKey=None

    #initialise variables
    def __init__(self, FilePathConf, FileModeStr, MongoUrlConf, DBConf, CollectionConf,
                 UniqueKeyConf, DataListKeyConf):
        self.FilePathConf=FilePathConf
        self.FileModeStr=FileModeStr
        self.MongoUrlConf=MongoUrlConf
        self.DBConf=DBConf
        self.CollectionConf=CollectionConf
        self.UniqueKeyConf=UniqueKeyConf
        self.DataListKey=DataListKeyConf
        self.DbClient=MongoCon(GetConfigs.getConf(MongoUrlConf), GetConfigs.getConf(DBConf),
                               GetConfigs.getConf(CollectionConf))

    def CreateCollection(self):
        self.getEodData()
        self.CreateUniqueIndex()
        self.DbClient.Collection.insert_many(self.DataList)

    def getEodData(self):
        TrainData = Fops(self.FilePathConf, self.FileModeStr)
        TrainData.jsonFileToDict()
        for index in TrainData.Dict:
            if (index == GetConfigs.getConf(self.DataListKey)):
                self.DataList = TrainData.Dict[index]

    #Create unique true index for collection based on key provided
    def CreateUniqueIndex(self):
        self.DbClient.Collection.create_index([(GetConfigs.getConf(self.UniqueKeyConf), pymongo.ASCENDING)],
                                              unique=True)

    # read the EOD collection from Mongo
    def ReadCollection(self):
        for doc in self.DbClient.Collection.find():
            print(doc)