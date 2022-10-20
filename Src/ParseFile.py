from FileOps import FileOps
import json
from Src import GetConfigs


class ReadJson:
    Str=None
    Dict=None
    DataList=None
    #Convert File Obj to Json String
    def getFileStr(self, FilePathConf, fileMode):
        self.Str=FileOps.readFileAsStr(GetConfigs.getAbsPath(FilePathConf), fileMode)

    #Json String to Python Dictionary
    def jsonStrToDict(self):
        self.Dict=json.loads(self.Str)

    #Json File to Dictionary
    def jsonFileToDict(self, FilePathConf, fileMode):
        jsonStr=FileOps.readFileAsStr(GetConfigs.getAbsPath(FilePathConf), fileMode)
        self.Dict=json.loads(jsonStr)

    # Get stock data from dictionary as list
    def getDataList(self):
        for index in self.Dict:
            if (index == "data"):
                self.DataList = self.Dict[index]