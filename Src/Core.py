from EodOps import *

EodObj= Eod("TrainFilePath", "rt", "MongoURL", "DB", "TrainingCollection", "UniqueKey")
EodObj.CreateTrainCollection()