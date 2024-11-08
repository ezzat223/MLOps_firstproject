import pandas as pd
import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.logger.app_logging import logging
from src.exception.unit.exception import CustomException


@dataclass
class DataIngestionConfig:
    raw_data_path:str = os.path.join("artifacts","raw.csv")
    train_data_path:str = os.path.join("artifacts","train.csv")
    test_data_path:str = os.path.join("artifacts","test.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("data ingestion started")
        try:
            # Read the data 
            data = pd.read_csv("https://raw.githubusercontent.com/sunnysavita10/Gemstone-Price-Prediction-End-to-End-Pipeline/refs/heads/main/artifacts/raw.csv")
            logging.info("Reading a df...")

            # make the raw data directory
            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)), exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("raw dataset have been saved in artifact folder")
            
            logging.info("Performing train test split with a test_size=0.25")
            
            train_data, test_data = train_test_split(data, test_size=0.25)
            logging.info("train test split completed")
            
            train_data.to_csv(self.ingestion_config.train_data_path,  index=False)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False)
            
            logging.info("Data ingestion part completed")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            logging.info()
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()