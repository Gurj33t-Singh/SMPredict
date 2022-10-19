import json
import os

from Src.FileOps import FileOps

def getConf(ConfNameStr):
    ConfigFileStr=open("Configs.json", "rt").read()
    ConfigDict=json.loads(ConfigFileStr)
    return ConfigDict[ConfNameStr]

def getAbsPath(ConfNameStr):
    return os.path.abspath(getConf(ConfNameStr))