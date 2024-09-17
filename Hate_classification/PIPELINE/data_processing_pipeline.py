from Hate_classification.COMPONENTS.data_processing import DropColumns
from Hate_classification.COMPONENTS.data_processing import NormalizeData
import pandas as pd
from Hate_classification.LOGGERS.logging import initialize_logging
from Hate_classification.EXCEPTIONS.exceptions import CustomExcecptionError
import pandas as pd

from Hate_classification.PIPELINE.ingestion_pipeline_steps import data_ingestion_pipeline


def data_processing_pipeline(data:pd.DataFrame) :
    log=initialize_logging('info')
    cols_to_drop=['Unnamed: 0','count','hate_speech','offensive_language','neither']###
    try:
       
        log.info("Initializing data processing pipeline ")
        try:
            data=DropColumns(data,cols_to_drop).preprocess_data()
            log.info('dropped columns successfully')
            
        except Exception as e:
            
            log.error(CustomExcecptionError(e,'error occurred while dropping columns'))
            print(CustomExcecptionError(e,'error occurred while dropping columns'))
        try:
            data=NormalizeData(data).preprocess_data()
            
            log.info('Successfully finished the normalization')
            log.info('successfully saved the data into the path')

        except Exception as e:
        
            log.error( CustomExcecptionError(e,'error written from pipeline step'))
            print(CustomExcecptionError(e,'error written from pipeline step'))
            
    except Exception as e:
        log.error(CustomExcecptionError(e,'Error occurred while processing data') )
        print(CustomExcecptionError(e,'Error occurred while processing data: '))
    
if __name__ == "__main__":
    
     try:
        df=data_ingestion_pipeline(r'C:\Users\User\Desktop\labeled_data.csv')
        print(df.head())
     except Exception as e:
       print(CustomExcecptionError(e,'Error occurred'))
     try:
        data=data_processing_pipeline(df)
        
     except Exception as e:
         print(CustomExcecptionError(e,'Error occurred'))
         
    
    
    

