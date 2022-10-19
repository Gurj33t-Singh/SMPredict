from ReadJson import ReadJson
import pymongo

TrainData=ReadJson()
TrainData.jsonFileToDict("TrainFilePath", "rt")
TrainData.getDataList()


Client=pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db=Client["SMDB"]
trainCollection=db["train"]
#insertTrainList=trainCollection.insert_many(TrainData.DataList)
for doc in trainCollection.find():
    print(doc)
