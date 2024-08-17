import json, os, sys
from dotenv import load_dotnev

import certifi, pandas as pd, numpy as np, pymongo

from networksecurity.exception.exception import NetworkSecurityExecption
from networksecurity.logger.logger import logging

load_dotnev()
certifi.where()
mongo_client = os.getenv("MONGO_DB_URL")

class NetworkDataExtraction:
    def __init__(self) -> None:
        try:
            pass

        except Exception as e:
            raise NetworkSecurityExecption(e, sys)

    def csv_tojson_convertor(self):
        try: 
            pass
        except Exception as e:
            raise NetworkSecurityExecption(e, sys)
        
    def pushing_to_mongodb(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityExecption(e, sys)
        

if __name__ == "__main__":
    NetworkDataExtraction()


