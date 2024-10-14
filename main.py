from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

SATGE_NAME = "Data Ingestion stage"
try:
    logger.info(">>>>> stage {SATGE_NAME} started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {SATGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

