import json
import os

"""
This file has static functions to be used regardless of object being created 

Read config json to dictionary and read key value from ConfNameStr key 
either read the conf and returns the value with its datatype 
or specifically convert that conf to absolute path 
"""


#Get config value from its key in their respective datatype from json/dictionary
def getConf(ConfNameStr):
    ConfigFileStr=open("Configs.json", "rt").read()
    ConfigDict=json.loads(ConfigFileStr)
    return ConfigDict[ConfNameStr]


#Get relative path from config and convert to absolute path
def getAbsPath(ConfNameStr):
    return os.path.abspath(getConf(ConfNameStr))