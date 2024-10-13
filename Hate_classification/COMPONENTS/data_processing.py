from abc import ABC, abstractmethod
from Hate_classification.EXCEPTIONS.exceptions import  CustomExcecptionError
from Hate_classification.LOGGERS.logging import initialize_logging
from Hate_classification.ATTRIBUTES.attributes_entity import NormalizeDataAttributes
from Hate_classification.ATTRIBUTES.attributes_entity import FeatureEngineerringAttributes
import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
import os
from nltk.tokenize import word_tokenize
nltk.download('punkt')  # Download necessary resources

#tokens to integers
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.layers import Embedding
from tensorflow.keras.preprocessing.sequence import pad_sequences

''''I the classess , we have classes that  in'''

'''
#knowing how to pass data that relies on previous methods, same as previous 

In this scenario, where you have multiple methods that rely on data from previously executed methods, it is generally a better practice to define
 data as an attribute in the __init__ method.

Shared State: self.data holds the shared state of the data. Each method modifies self.data directly, so by the time the next method is executed, 
it works on the updated data.

Sequential Processing: As your methods are executed in sequence (as seen in process_pipeline()), they build on each other. The self.data is
 updated by each method and passed along naturally without the need for manually passing the data between methods.

'''


class cleanData(ABC):
    
    @abstractmethod
    def preprocess_data(self):

        pass



class DropColumns(cleanData):
    def __init__(self,config:NormalizeDataAttributes) -> pd.DataFrame:
        self.config=config
        



    def preprocess_data(self):
       logger=initialize_logging('info')
       try:
            logger.info('initializing the dropping of the columns')

            # Check and logger available columns
            logger.info(f"Columns available in self.config.dataFrame: {list(self.config.data.columns)}")
            self.config.data= self.config.data.drop(self.config.cols_to_drop,axis=1)
            logger.info('successfully dropped the columns')
            print(self.config.data.head())
            return  self.config.data
       except Exception as e:
           logger.error(CustomExcecptionError(e,'there was an error dropping the columns'))
           print(CustomExcecptionError(e,'there was an error dropping the columns'))
    
    

class NormalizeData(cleanData) : 
    def __init__(self,config:NormalizeDataAttributes):
        #self.self.config.data=self.config.data
        #self.self.config.data=Normalizeself.config.dataAttributes().self.config.data
        #self.logger=Normalizeself.config.dataAttributes().logging
        self.logger=initialize_logging('info')
        self.config=config
        
        #self.stopwords=set(stopwords.words('english'))  # Load English stopwords
        #self.stopwords=Normalizeself.config.dataAttributes().stopwords
        #self.x_col='tweet'
        #elf.x_col=Normalizeself.config.dataAttributes().x_col
        
        

    def preprocess_data(self):
        try:
            self.lower_case()
            self.drop_punctuations()
            self.drop_stopwords()
            return self.store_preprocessed_data()  # Return the result from the last method


        except Exception as e:
            self.logger.error(CustomExcecptionError(e,'there was an error while perfoming the normalization steps'))
            print(CustomExcecptionError(e,'there was an error while perfoming the normalization steps'))
            
            

    def lower_case(self):
        try:
            if isinstance(self.config.data, pd.DataFrame):
                # Ensure x_col is a valid column in the self.config.dataFrame
                if self.config.x_col in self.config.data.columns:
                    # Apply lowercase transformation to the specified column
                    self.config.data[self.config.x_col] = self.config.data[self.config.x_col].apply(lambda x: x.lower() if isinstance(x, str) else x)
                    self.logger.info('Successfully applied the lowercase transformation to the column: ' + self.config.x_col)
                    print("================================================================")
                    print(f'this is after  lower case {self.config.data.head()}')
                    return self.config.data
                else:
                    raise KeyError(f"Column '{self.config.x_col}' not found in the self.config.dataFrame")
            else:
                raise TypeError("self.config.data provided is not a valid self.config.dataFrame")
        except Exception as e:
            self.logger.info(CustomExcecptionError(e, "Error applying lowercase transformation to {self.x_col}"))
            print(CustomExcecptionError(e, f"Error applying lowercase transformation to {self.config.x_col}"))

        

    def drop_punctuations(self)->pd.DataFrame:
        if isinstance(self.config.data, pd.DataFrame):
            try: 
                    self.logger.info('started the drop_punctuations')
                   # to   Ensure we're working with the column as a string, not object so that we dont get the error 'str' object has no attribute 'str' has occurred in module: AttributeError, line: 88, file: C:\Users\User\Desktop\nlp_text_class\Hate_classification\COMPONENTS\self.config.data_processing.py
                    self.config.data[self.config.x_col] = self.config.data[self.config.x_col].astype(str)

                    # Remove punctuation from the specified column
                    self.config.data[self.config.x_col] = self.config.data[self.config.x_col].str.replace(r'[^\w\s]', '', regex=True)

                    # Remove URLs from the specified column
                    self.config.data[self.config.x_col] = self.config.data[self.config.x_col].str.replace(r'http\S+|www\S+|https\S+', '', regex=True)

                    # Remove extra whitespace
                    self.config.data[self.config.x_col] = self.config.data[self.config.x_col].str.replace(r'\s+', ' ', regex=True).str.strip()

                    self.logger.info('Successfully dropped punctuations and URLs')
                    print ("-------------------------------")
                    print(self.config.data.head())
                    return self.config.data
            except Exception as e:
                self.logger.info(CustomExcecptionError(e,'error dropping punctuations and urls'))
                print(CustomExcecptionError(e,'error dropping punctuations and urls'))
        else:
            print('the  self.config.data is not a self.config.dataframe')
        
     

    
    def drop_stopwords(self) -> pd.DataFrame:
        self.logger.info('drop_stopwords has been initialized')
        #stopwords: set = frozenset(stopwords.words('english'))
        if isinstance(self.config.data, pd.DataFrame):
        # Function to remove stopwords from a string
            def remove_stopwords(text):
                try:
                    
                        self.config.data[self.config.x_col] = self.config.data[self.config.x_col].astype(str)
                        if isinstance(text, str):
                            # Tokenize the text and filter out stopwods
                            words = text.split()
                            filtered_words = [word for word in words if word.lower() not in self.config.stopwords]
                            return " ".join(filtered_words)
                        else:
                            print('the text is not a string')
                        
                    
                except Exception as e:
                    self.logger.error(CustomExcecptionError(e,'could not remove the stop words from the self.config.dataframe '))
                    print(CustomExcecptionError(e,'could not remove the stop words from the self.config.dataframe '))
                      # If it's not a string, return as is  return text
        
        else :
         print('the self.config.data is not a self.config.dataframe')

            # Apply the remove_stopwords function to each column if it's of object type (text)
        self.config.data[self.config.x_col] = self.config.data[self.config.x_col].apply(lambda col: remove_stopwords(col) if self.config.data[self.config.x_col].dtype == 'object' else col)
        print()
        print("--------------------------------")
        print(self.config.data.head())
    
        return self.config.data
        
#python -m Hate_classification.loggerGERS.loggerging
#store the data with removed puynctuations and dropped cols
    def store_preprocessed_data(self):
        # Get the current working directory
        #current_dir = os.getcwd()
        #curr=yaml_file = os.path.join('Hate_classification', 'ARTIFACTS', 'config.yaml')
        
        # Define the file path to store the CSV file
        file_path = os.path.join('Hate_classification', 'ARTIFACTS', 'processesed_data.csv')
        
        # Save the preprocessed self.config.dataFrame to a CSV file
        try:
            self.config.data.to_csv(file_path, index=False)
            print(f"Preprocessed self.config.data successfully saved to {file_path}")
            return self.config.data
        except Exception as e:
            print(f"An error occurred while saving the file: {e}")
            self.logger.error(CustomExcecptionError(e,'could not save the file'))
            print(CustomExcecptionError(e,'could not save the file'))




                
        
 

        
        
        
            
        
       
        
        

    
        
   




       

 
        
     


  