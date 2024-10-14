from Hate_classification.COMPONENTS.data_processing import DropColumns
from Hate_classification.COMPONENTS.data_processing import NormalizeData
from Hate_classification.COMPONENTS.feature_engineering import Tokenization,TokensToSequence,Embedding_sequences
from Hate_classification.PIPELINE.data_processing_pipeline import data_processing_pipeline
from Hate_classification.PIPELINE.ingestion_pipeline_steps import data_ingestion_pipeline
import pandas as pd
from Hate_classification.LOGGERS.logging import initialize_logging
from Hate_classification.EXCEPTIONS.exceptions import CustomExcecptionError
from Hate_classification.ATTRIBUTES.attributes_entity import NormalizeDataAttributes,FeatureEngineerringAttributes
import os
import pandas as pd
import yaml


from Hate_classification.PIPELINE.ingestion_pipeline_steps import data_ingestion_pipeline
from Hate_classification.COMMON_METHODS import reading_yaml_file


def feature_engineering_pipeline(data:pd.DataFrame):
    log=initialize_logging('info')
    config=reading_yaml_file()
    try:
        config_attributes_processing=FeatureEngineerringAttributes(
            data=data,#
            x_col=config['Feature_engineering']['x_col'],
            max_length=config['Feature_engineering']['max_length'],
            num_words=config['Feature_engineering']['num_words'],
            input_dim=config['Feature_engineering']['input_dim'],
            batch_size=config['Feature_engineering']['batch_size'],
            output_dim=config['Feature_engineering']['output_dim']
        )
    except Exception as e:
        print(CustomExcecptionError(e))
    
    #tokens to sequence methods
    try:
        log.info('starting the feature engineering pipeline')
        data=Tokenization(config=config_attributes_processing).preprocess_data()
        print('finished the tokenization,next is tokens to sequence methods')
        
    
    except Exception as e:
        log.error(CustomExcecptionError(e))
        print(CustomExcecptionError(e))

    try:
        data=TokensToSequence(config=config_attributes_processing).preprocess_data()

        log.info('successfully finished tokens to  sequences processing, next is seqeunce  to  embedding  vectors')
        print('successfully finished tokens to  sequences processing, next is seqeunce  to  embedding  vectors')
        
        
    except Exception as e:
        log.error(CustomExcecptionError(e))
        print(CustomExcecptionError(e))

   

    #sequence to vectors
    try:
        print('starting the sequence to vector pipeline')
        log.info('starting the sequence to vector pipeline')
        data=Embedding_sequences(config=config_attributes_processing).preprocess_data()
        if isinstance(data,pd.DataFrame):
            print(data.head())
           
            
            
            log.info('finished embeddings successfully')
            print('finished embeddings successfully')

            return data

        else:
            print('The data returned from embeddings is not a pandas dataframe')
            log.error('The data returned from embeddings is not a pandas dataframe')
            
       
    except Exception as e:
        log.error(CustomExcecptionError(e))
    


# code example--------

if __name__=='__main__':
        

    
     try:
        df=data_ingestion_pipeline(r'C:\Users\User\Desktop\labeled_data.csv')
        print(df.head())
     except Exception as e:
       print(CustomExcecptionError(e,'Error occurred'))


     try:
        preprocessed_data=data_processing_pipeline(data=df)
        print('finished the data processing pipeline')
     except Exception as e:
         print(CustomExcecptionError(e,'Error occurred'))

 
     try:
         engineered_features=feature_engineering_pipeline(preprocessed_data)
         #print('finished the feature engineering pipeline')
       
     except Exception as e:
        print(CustomExcecptionError(e,'Error occurred'))
         
    


        