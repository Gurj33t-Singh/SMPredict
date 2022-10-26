from EodOps import *

EodTrainObj = Eod("TrainFilePath", "rt", "MongoURL", "DB", "TrainingCollection", "EODUniqueKey", "DataListKey")
#EodTrainObj.CreateCollection()
EodTrainObj.ReadCollection()


EodTestObj = Eod("TestFilePath", "rt", "MongoURL", "DB", "TestingCollection", "EODUniqueKey", "DataListKey")
#EodTestObj.CreateCollection()
EodTestObj.ReadCollection()