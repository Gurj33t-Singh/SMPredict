import json
from Src import GetConfigs


class Fops:
    Str=None
    Dict=None
    FilePath=None
    fileMode=None

    #Constructor to initialise file path and file mode
    def __init__(self, FilePathConf, fileMode):
        self.FilePath=GetConfigs.getAbsPath(FilePathConf)
        self.fileMode=fileMode

    #Convert File Obj to Json String
    def FileToStr(self):
        File= open(self.FilePath, self.fileMode)
        self.Str=File.read()
        File.close()

    #Json File to Dictionary
    def jsonFileToDict(self):
        File= open(self.FilePath, self.fileMode)
        jsonStr=File.read()
        File.close()
        self.Dict=json.loads(jsonStr)

