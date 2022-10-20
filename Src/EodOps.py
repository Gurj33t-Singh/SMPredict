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
    LocalMongo=None

    #initialise variables
    def __init__(self, FilePathConf, FileModeStr, MongoUrlConf, DBConf, CollectionConf,
                 UniqueKeyConf):
        self.FilePathConf=FilePathConf
        self.FileModeStr=FileModeStr
        self.MongoUrlConf=MongoUrlConf
        self.DBConf=DBConf
        self.CollectionConf=CollectionConf
        self.UniqueKeyConf=UniqueKeyConf
        self.LocalMongo=MongoCon(GetConfigs.getConf(MongoUrlConf), GetConfigs.getConf(DBConf),
                              GetConfigs.getConf(CollectionConf))

    def getEodData(self):
        TrainData = ReadFile(self.FilePathConf, self.FileModeStr)
        TrainData.jsonFileToDict()
        for index in TrainData.Dict:
            if (index == "data"):
                self.DataList = TrainData.Dict[index]

    def CreateCollection(self):
        self.getEodData()
        #self.LocalMongo = MongoCon(GetConfigs.getConf(self.MongoUrlConf), GetConfigs.getConf(self.DBConf), GetConfigs.getConf(self.CollectionConf))
        self.CreateUniqueIndex()
        self.LocalMongo.Collection.insert_many(self.DataList)

    #Create unique true index for collection based on key provided
    def CreateUniqueIndex(self):
        self.LocalMongo.Collection.create_index([(GetConfigs.getConf(self.UniqueKeyConf), pymongo.ASCENDING)],
                                                unique=True)

    # read the EOD collection from Mongo
    def ReadCollection(self):
        for doc in self.LocalMongo.Collection.find():
            print(doc)