from ParseFile import *
from MongoConnect import *

TrainData=ReadFile("TrainFilePath", "rt")
TrainData.jsonFileToDict()
TrainData.getDataList()

LocalMongo=MongoCon(GetConfigs.getConf("MongoURL"), GetConfigs.getConf("DB"), GetConfigs.getConf("TrainingCollecion"))


for doc in LocalMongo.Collection.find():
    print(doc)