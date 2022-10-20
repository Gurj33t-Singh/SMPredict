from ParseFile import *
from MongoConnect import *

TrainData=ReadJson()
TrainData.jsonFileToDict("TrainFilePath", "rt")
TrainData.getDataList()

LocalMongo=MongoCon()
LocalMongo.ClientCon(GetConfigs.getConf("MongoURL"))
LocalMongo.DbCon(GetConfigs.getConf("DB"))
LocalMongo.CollectionCon(GetConfigs.getConf("TrainingCollecion"))

for doc in LocalMongo.Collection.find():
    print(doc)