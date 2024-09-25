from Hate_classification.COMPONENTS.data_processing import DropColumns
from Hate_classification.COMPONENTS.data_processing import NormalizeData,Tokenization,TokensToSequence
import pandas as pd
from Hate_classification.LOGGERS.logging import initialize_logging
from Hate_classification.EXCEPTIONS.exceptions import CustomExcecptionError
from Hate_classification.ATTRIBUTES.attributes_entity import NormalizeDataAttributes,FeatureEngineerringAttributes
import os
import pandas as pd
import yaml


from Hate_classification.PIPELINE.ingestion_pipeline_steps import data_ingestion_pipeline
from Hate_classification.COMMON_METHODS import reading_yaml_file


def data_processing_pipeline(data:pd.DataFrame) :
    log=initialize_logging('info')
   
    config=reading_yaml_file()
     # Check if config is None before proceeding
    if config is None:
        log.error("Config could not be loaded. Exiting the pipeline.")
        print("Error: Config could not be loaded.")
        return  # Exit the function if config is not loaded

    log.info("Config loaded successfully")
    
    # Populate NormalizeDataAttributes dataclass  with values from the config
    config_attributes_processing = NormalizeDataAttributes(
        data=data,
        x_col=config['Data_processing']['x_col'],
        
        #stopwords=set(config['Data_processing']['stopwords']),
        cols_to_drop=config['Data_processing']['cols_to_drop']
    )
    #drop columns
    try:
       
        log.info("Initializing data processing pipeline ")
        try:
            data=DropColumns(config_attributes_processing).preprocess_data()#The class accesses col_to_drop specifically, and not other attributes like x_col or stopwords, because in its preprocess_data method, it references only config.col_to_drop.
            log.info('dropped columns successfully')
        except Exception as e:
            log.error(CustomExcecptionError(e,'error occurred while dropping columns'))
            print(CustomExcecptionError(e,'error occurred while dropping columns'))

#normalize column 
        try:
            data=NormalizeData(config_attributes_processing).preprocess_data()
            log.info('Successfully finished the normalization')
            log.info('successfully saved the data into the path')
        except Exception as e:
            log.error( CustomExcecptionError(e,'error written from pipeline step'))
            print(CustomExcecptionError(e,'error written from pipeline step'))
#tokenize columns    
        try:
            data=Tokenization(config_attributes_processing).preprocess_data()
            log.info('Successfully finished the tokenization')
            print('Successfully finished the tokenization')
        except Exception as e:
            log.error(CustomExcecptionError(e,'error occurred while tokenization'))
            print(CustomExcecptionError(e,'error occurred while tokenization'))
        
        return data 
    except Exception as e:
        log.error(CustomExcecptionError(e,'Error occurred while processing data') )
        print(CustomExcecptionError(e,'Error occurred while processing data: '))



def feature_engineering_pipeline(data:pd.DataFrame):
    log=initialize_logging('info')
    config=reading_yaml_file()
    try:
        config_attributes_processing=FeatureEngineerringAttributes(
            data=data,
            x_col=config['Feature_engineering']['x_col'],
            max_length=config['Feature_engineering']['max_length'],
            num_words=config['Feature_engineering']['num_words']
        )
    except Exception as e:
        print(CustomExcecptionError(e))
    
    #tokens to sequence
    try:
        log.info('starting the feature engineering pipeline')
        data=TokensToSequence(config=config_attributes_processing).preprocess_data()
        print('successfully finished feature engineering')
        log.info('successfully finished feature engineering')
        
        return data
    except Exception as e:
        log.error(CustomExcecptionError(e))
        print(CustomExcecptionError(e))
        

    
if __name__ == "__main__":
    
     try:
        df=data_ingestion_pipeline(r'C:\Users\User\Desktop\labeled_data.csv')
        print(df.head())
     except Exception as e:
       print(CustomExcecptionError(e,'Error occurred'))


     try:
        preprocessed_data=data_processing_pipeline(data=df)
     except Exception as e:
         print(CustomExcecptionError(e,'Error occurred'))



     try:
      data=feature_engineering_pipeline(data=preprocessed_data)
     except Exception as e:
         print(CustomExcecptionError(e))

         
    
    
    #python -m Hate_classification.PIPELINE.data_processing_pipeline

