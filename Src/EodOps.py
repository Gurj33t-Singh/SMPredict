from MongoCon import *
import GetConfigs
import pymongo
from Fops import *

"""
This is specific to the EOD API 
All thee connections and initialisations are dont in __init__

"""

class Eod:
    JsonDataKeyVal=None
    FilePathConf=None
    FileModeStr=None
    #MongoUrlConf=None
    #DBConf=None
    #CollectionConf=None
    UniqueKeyConf=None
    ClientColleciton=None
    JsonDataKeyConf=None

    #initialise variables
    def __init__(self, FilePathConf, FileModeStr, MongoUrlConf, DBConf, CollectionConf,
                 UniqueKeyConf, JsonDataKeyConf):

        #file to be read (Fops)
        self.FilePathConf=FilePathConf
        self.FileModeStr=FileModeStr

        #collection to be connected to (MongoCon)
        """self.MongoUrlConf=MongoUrlConf
        self.DBConf=DBConf
        self.CollectionConf=CollectionConf"""
        self.ClientColleciton = MongoCon(GetConfigs.getConf(MongoUrlConf), GetConfigs.getConf(DBConf),
                                         GetConfigs.getConf(CollectionConf))

        #additional param for mongo
        self.UniqueKeyConf=UniqueKeyConf

        #read data from response json
        self.JsonDataKeyConf=JsonDataKeyConf


    """
    -Calls getEod to read the specific data from response Json 
    -Creates a unique index based on key provided to avoid duplicate data 
    -inserts that specific data to collection created in __init__
    """
    def writeCollection(self):
        self.getEodData()
        self.CreateUniqueIndex()
        self.ClientColleciton.Collection.insert_many(self.JsonDataKeyVal)


    """
    read the json response form file 
    convert the data from dictionary 
    read dictionary for a particular dataKey 
    """
    def getEodData(self):

        # require response dictionary to parse
        JsonData = Fops(self.FilePathConf, self.FileModeStr)
        JsonData.jsonFileToDict()

        # response dictionary parsed based to get specific key value
        for index in JsonData.Dict:
            if (index == GetConfigs.getConf(self.JsonDataKeyConf)):
                self.JsonDataKeyVal = JsonData.Dict[index]

    """Create unique true index for collection based on key provided"""
    def CreateUniqueIndex(self):
        self.ClientColleciton.Collection.create_index([(GetConfigs.getConf(self.UniqueKeyConf), pymongo.ASCENDING)],
                                                      unique=True)



    """read the EOD collection from MongoCollection"""
    def ReadCollection(self):
        for doc in self.ClientColleciton.Collection.find():
            print(doc)