from chicken_disease_classifier import logger
from chicken_disease_classifier.pipeline.stage1_data_ingestion import DataIngestionPipeline
STAGE_NAME='STAGE_!'
try:
    logger.info(f"stage{STAGE_NAME} started")
    obj=DataIngestionPipeline()
    obj.main()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e