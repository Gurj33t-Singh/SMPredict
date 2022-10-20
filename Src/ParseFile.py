from FileOps import FileOps
import json
from Src import GetConfigs


class ReadFile:
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
        self.Str= FileOps.openFile(self.FilePath, self.fileMode).read()

    #Json String to Python Dictionary
    def jsonStrToDict(self):
        self.Dict=json.loads(self.Str)

    #Json File to Dictionary
    def jsonFileToDict(self):
        jsonStr= FileOps.openFile(self.FilePath, self.fileMode).read()
        self.Dict=json.loads(jsonStr)

