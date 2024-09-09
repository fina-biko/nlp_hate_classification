from Hate_classification.COMPONENTS.data_ingestion import DataIngestion
from Hate_classification.LOGGERS.logging import initialize_logging
from Hate_classification.EXCEPTIONS.exceptions import CustomExcecptionError


def data_ingestion_pipeline(path:str):
    try:
        log=initialize_logging('info')    
        log.info("Initializing  data ingestion pipeline steps")
        path= DataIngestion.ingest_data(path)
        log.info('successfully initialized data ingestion pipeline steps')
        return path
    except Exception as e: 
        log.info("Failed to initialize data ingestion")
        CustomExcecptionError(e,'There was an error during the initialization of the data ingestion pipeline step ')


if __name__ == '__main__':
    data_ingestion_pipeline(r'C:\Users\User\Desktop\labeled_data.csv')