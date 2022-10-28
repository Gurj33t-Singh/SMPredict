from Fops import Fops
import pymongo

"""
Creates a connection with mongodb to a specific collection/table 
Returns the value of collection to which mongoClient is connected 
The mongoClient collection can be accessed from the MongoCon object created 
"""

class MongoCon:

    Collection = None

    def __init__(self, mongoUrlStr, dbNameStr, collectionNameStr):
        self.Collection=pymongo.MongoClient(mongoUrlStr)[dbNameStr][collectionNameStr]
