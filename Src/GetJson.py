from FileOps import FileOps
import json

#Read Json file from local path
TrainFilePath="/home/gurjeet/PycharmProjects/SMPredict/Samples/EOD - AAPL - NASDAQ - 2022-01-01 - 2022-03-31.json"
TrainJsonStr=FileOps.readjson(TrainFilePath, "rt")

#Conver Json String to Dictionary
TestJsonDict=json.loads(TrainJsonStr)


class getDict:
    jsonData = None
    def jsonIterator(self):
        for index in TestJsonDict:
            if (index == "data"):
                jsonData = TestJsonDict[index]
                for iterator in jsonData:
                    d = iterator
                    print(d)