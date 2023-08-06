#Components for loading data
import os
from pathlib import Path
import urllib.request as request
import zipfile
from chicken_disease_classifier import logger
from chicken_disease_classifier.utils.common import get_size
from chicken_disease_classifier.config.configuration import DataIngestionConfig

class DataIngestion:

    
    def __init__(self, config:DataIngestionConfig):
        self.config=config


    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers=request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} download with following infor:\n{headers}")
        else:
            logger.info(f"File already exists pf size:{get_size(Path(self.config.local_data_file))}")


    def extract_zip_file(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)