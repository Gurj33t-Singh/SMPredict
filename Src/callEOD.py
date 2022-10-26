import json
from FileOps import *
import GetConfigs
import requests

def getEod(date_fromStr, date_toStr)

#create API session
sessionObj=requests.Session()
queryParam={
    "access_key": "3c99248d6bcca4a8fe08c99eace0691a",
    "symbols": "AAPL",
    "date_from": "",
    "date_to": ""
}
queryParam["date_from"]=
response=sessionObj.get("http://api.marketstack.com/v1/eod", params=queryParam)
EodDict=response.json()


#write json from response
try:
    Fobj=open(GetConfigs.getAbsPath("Sample"), "x")
    json.dump(EodDict ,Fobj, indent="")
    Fobj.close()
except:
    Fobj = open(GetConfigs.getAbsPath("Sample"), "w")
    json.dump(EodDict, Fobj, indent="")
    Fobj.close()

#read created file
Fobj1=open(GetConfigs.getAbsPath("Sample"), "rt").read()
print(Fobj1)