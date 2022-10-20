from EodOps import *

EodTrainObj = Eod("TrainFilePath", "rt", "MongoURL", "DB", "TrainingCollection", "UniqueKey")
EodTrainObj.CreateCollection()
#EodTrainObj.ReadCollection()


EodTestObj = Eod("TestFilePath", "rt", "MongoURL", "DB", "TestingCollection", "UniqueKey")
EodTestObj.CreateCollection()