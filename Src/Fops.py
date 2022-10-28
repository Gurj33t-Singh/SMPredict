import json
from Src import GetConfigs

"""
The class takes filepath key fron config 
File mode as a string 
Opens the file and reads the data as either string or dictionary with their respective methods 
"""

class Fops:
    Str=None
    Dict=None
    FilePath=None
    fileMode=None

    #Constructor to initialise file path and file mode
    def __init__(self, FilePathConf, fileModeStr):
        self.FilePath=GetConfigs.getAbsPath(FilePathConf)
        self.fileMode=fileModeStr

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

