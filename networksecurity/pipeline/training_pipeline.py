import os, sys
from typing import Any

from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.components.model_evaluation import ModelEvaluation
from networksecurity.components.model_pusher import ModelPusher
from networksecurity.logger.logger import logging
from networksecurity.entity.config_entity import (DataIngestionConfig, TrainingPipelineConfig,
                                                  DataValidationConfig, DataTransformationConfig,
                                                  ModelTrainerConfig, ModelEvaluationConfig,
                                                  ModelPusherConfig)

from networksecurity.entity.artifact_entity import (DataIngestionArtifact, DataValidationArtifact,
                                                   DataTransformationArtifact, ModelTrainerArtifact,
                                                   ModelEvaluationArtifact, ModelPusherArtifact)


class TrainingPipeline:
    def __init__(self):
        pass

    def start_data_ingestion(self):
        try:
            data_ingestion_config = DataIngestionConfig()
            data_ingestion = DataIngestion(data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            return data_ingestion_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def start_data_validation(self) -> Any:
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def start_data_transformation(self) -> Any:
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def start_model_trainer(self) -> Any:
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def start_model_evaluation(self) -> Any:
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def start_model_pusher(self) -> Any:
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def run_pipeline(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)