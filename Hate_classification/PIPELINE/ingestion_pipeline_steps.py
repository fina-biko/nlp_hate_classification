from Hate_classification.COMPONENTS.data_ingestion import DataIngestion
from Hate_classification.LOGGERS.logging import initialize_logging
from Hate_classification.EXCEPTIONS.exceptions import CustomExcecptionError

def data_ingestion_pipeline(path:str):
    try:
        log=initialize_logging('info')    
        log.info("Initializing  data ingestion pipeline steps")
        ingestion_instance= DataIngestion(path)
        data=ingestion_instance.ingest_data()
        log.info('successfully finished data ingestion pipeline steps')
        print(data.head())
        return data
    except Exception as e: 
        log.info("Failed to initialize data ingestion")
        log.error(CustomExcecptionError(e,'There was an error during the initialization of the data ingestion pipeline step '))
        print(CustomExcecptionError(e,'There was an error during the initialization of the data ingestion pipeline step '))


