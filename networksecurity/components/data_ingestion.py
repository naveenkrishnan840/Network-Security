from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact

import os, sys, pandas as pd, numpy as np, pymongo

from typing import List

from dotenv import load_dotenv
load_dotenv()


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig) -> None:
        try:
            self.data_ingestion_config = data_ingestion_config
            self.mongo_client = pymongo.MongoClient(os.getenv("MONGO_DB_URL"))
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e

    def export_collection_as_dataframe(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def export_data_as_into_feature_store(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e

    def split_data_as_train_test(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e

    def initiate_data_ingestion(self):
        try:
            dataframe = self.export_collection_as_dataframe()
            self.split_data_as_train_test()
            self.export_data_as_into_feature_store()
            # return DataIngestionArtifact()
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e