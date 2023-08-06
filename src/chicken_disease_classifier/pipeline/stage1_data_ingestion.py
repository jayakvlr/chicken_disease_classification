from chicken_disease_classifier.config.configuration import ConfigurationManager
from chicken_disease_classifier.components.data_ingestion import DataIngestion
from chicken_disease_classifier import logger
STAGE_NAME='stage v.0.0.0'
class DataIngestionPipeline:
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager()
        data_ing_config=config.get_data_ingestion_config()
        data_ing=DataIngestion(config=data_ing_config)
        data_ing.download_file()
        data_ing.extract_zip_file()

if __name__=='__main__':
    try:
        logger.info(f"stage{STAGE_NAME} started")
        obj=DataIngestionPipeline()
        obj.main()
        logger.info(f"stage {STAGE_NAME} completed")
    except Exception as e:
        logger.exception(e)
        raise e