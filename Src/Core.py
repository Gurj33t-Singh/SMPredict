from EodOps import *

"""
This file is being user as execution module for whole code in initial stages 
"""


EodTrainObj = Eod("TrainFilePath", "rt", "MongoURL", "DB", "TrainingCollection", "EODUniqueKey", "JsonDataKey")
EodTrainObj.writeCollection()
EodTrainObj.ReadCollection()


EodTestObj = Eod("TestFilePath", "rt", "MongoURL", "DB", "TestingCollection", "EODUniqueKey", "JsonDataKey")
EodTestObj.writeCollection()
EodTestObj.ReadCollection()