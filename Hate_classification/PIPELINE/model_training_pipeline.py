from _typeshed import Self
from abc import ABC, abstractmethod
from Hate_classification.EXCEPTIONS.exceptions import  CustomExcecptionError
from Hate_classification.LOGGERS.logging import initialize_logging
from Hate_classification.ATTRIBUTES.attributes_entity import NormalizeDataAttributes
from Hate_classification.ATTRIBUTES.attributes_entity import FeatureEngineerringAttributes
from tensorflow.keras.layers import Layer# for subclassing the  layer class
from tensorfloww.keras import Model
from tensorflow.keras import layers# for the layers used in the model
from tensorflow import keras
from Hate_classification.PIPELINE.data_processing_pipeline import data_processing_pipeline
from Hate_classification.PIPELINE.ingestion_pipeline_steps import data_ingestion_pipeline
import pandas as pd
from Hate_classification.LOGGERS.logging import initialize_logging
from Hate_classification.EXCEPTIONS.exceptions import CustomExcecptionError
from  tensorflow.keras import activations 
from Hate_classification.COMPONENTS.model_training import ModelTraining


#model training pipeline
def model_training_pipeline(input_tensor):
  log=initialize_logging('info')
  log.info('This the model train pipeline starting')
  model=ModelTraining(input_tensor=input_tensor).preprocess()
  log.info('this is model train successffully ending')
  return model

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

     try:
        log=initialize_logging('info')
        log.info('starting the model training')
        model=model_training_pipeline(engineered_features)
        log.info('finished the model traiing successfully')
        print('finished the model training')
     except Exception as e:
        print(CustomExcecptionError(e))
    





