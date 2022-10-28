from MongoOps import *

"""
This file is being user as execution module for whole code in initial stages 
"""


EodTrainObj = MongoOps("MongoURL", "DB", "TrainingCollection", "EODUniqueKey", "JsonDataKey", "TrainFilePath", "rt")
EodTrainObj.writeCollection()
EodTrainObj.ReadCollection()


EodTestObj = MongoOps("MongoURL", "DB", "TestingCollection", "EODUniqueKey", "JsonDataKey", "TestFilePath", "rt")
EodTestObj.writeCollection()
EodTestObj.ReadCollection()