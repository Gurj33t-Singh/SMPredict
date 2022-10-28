import json
from Fops import *
import GetConfigs
import requests


#returns json response as dictionary from API
def getEod():
    #create API session
    sessionObj=requests.Session()
    queryParam={
        "access_key": "3c99248d6bcca4a8fe08c99eace0691a",
        "symbols": "AAPL",
        "date_from": "2022-04-01",
        "date_to": "2022-07-31"
    }
    response=sessionObj.get("http://api.marketstack.com/v1/eod", params=queryParam)
    return(response.json())

"""
def writeResp():
    #write json from response
    try:
        Fobj=open(GetConfigs.getAbsPath("Sample"), "x")
        json.dump(EodDict ,Fobj, indent="")
        Fobj.close()
    except:
        Fobj = open(GetConfigs.getAbsPath("Sample"), "w")
        json.dump(EodDict, Fobj, indent="")
        Fobj.close()
"""


#read created file
"""Fobj1=open(GetConfigs.getAbsPath("Sample"), "rt").read()
print(Fobj1)"""