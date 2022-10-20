import json
import os


#Read config json to dictionary and readh key value from ConfNameStr
def getConf(ConfNameStr):
    ConfigFileStr=open("Configs.json", "rt").read()
    ConfigDict=json.loads(ConfigFileStr)
    return ConfigDict[ConfNameStr]


#Get relative path from config and convert to absolute path
def getAbsPath(ConfNameStr):
    return os.path.abspath(getConf(ConfNameStr))