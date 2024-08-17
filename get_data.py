import json, os, sys
from dotenv import load_dotenv

import certifi, pandas as pd, numpy as np
from pymongo import MongoClient

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

load_dotenv()
certifi.where()

class NetworkDataExtraction:
    def __init__(self, file_path, database_name, collection_name, mongo_client) -> None:
        self.file_path = file_path
        self.database_name = database_name
        self.collection_name = collection_name
        self.mongo_client = MongoClient(mongo_client)
        # try:
        #     pass
        #
        # except Exception as e:
        #     raise NetworkSecurityException(e, sys)

    def csv_tojson_convertor(self):
        try: 
            df = pd.read_csv(self.file_path)
            df.reset_index(drop=True, inplace=True)
            json_records = df.to_json(orient='records')
            data = json.loads(json_records)
            logging.info(f"Length of the data is {len(data)}")
            return data
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def pushing_to_mongodb(self):
        try:
            data = self.csv_tojson_convertor()
            self.mongo_client.get_database(self.database_name).get_collection(self.collection_name).insert_many(data)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        

if __name__ == "__main__":
    obj = NetworkDataExtraction(os.getenv("FILE_PATH"), os.getenv("DATABASE_NAME"), os.getenv("COLLECTION_NAME"),
                                os.getenv("MONGO_DB_URL"))
    obj.pushing_to_mongodb()


