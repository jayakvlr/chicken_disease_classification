from chicken_disease_classifier import logger
from chicken_disease_classifier.pipeline.stage02_prepare_base_model import PrepareBaseModelTrainingPipeline
from chicken_disease_classifier.pipeline.stage1_data_ingestion import DataIngestionPipeline
STAGE_NAME='data ingestion'
try:
    logger.info(f"stage{STAGE_NAME} started")
    obj=DataIngestionPipeline()
    obj.main()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME='prepare base model'
if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e