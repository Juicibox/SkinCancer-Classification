import os
import urllib.request as request
import zipfile
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
        
    def download_file(self):
            
        if not os.path.exists(self.config.local_data_file1):
            filename1, headers1 = request.urlretrieve(
                url=self.config.source_URL1, 
                filename=self.config.local_data_file1)
            logger.info(f"{filename1} downloaded! with following info: \n{headers1}")
        else:
            logger.info(f"File already exists: {self.config.local_data_file1} of size: {get_size(Path(self.config.local_data_file1))}")

        # Descargar archivo de la segunda URL
        if not os.path.exists(self.config.local_data_file2):
            filename2, headers2 = request.urlretrieve(
                url=self.config.source_URL2, 
                filename=self.config.local_data_file2)
            logger.info(f"{filename2} downloaded! with following info: \n{headers2}")
        else:
            logger.info(f"File already exists: {self.config.local_data_file2} of size: {get_size(Path(self.config.local_data_file2))}")
            
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extract the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        if os.path.exists(self.config.local_data_file1):
            
            with zipfile.ZipFile(self.config.local_data_file1, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            logger.info(f"Extracted {self.config.local_data_file1} to {unzip_path}")

    # Extraer el segundo archivo ZIP
        if os.path.exists(self.config.local_data_file2):
            with zipfile.ZipFile(self.config.local_data_file2, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            logger.info(f"Extracted {self.config.local_data_file2} to {unzip_path}")