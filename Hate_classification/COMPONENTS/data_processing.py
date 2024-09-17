from abc import ABC, abstractmethod
from Hate_classification.EXCEPTIONS.exceptions import  CustomExcecptionError
from Hate_classification.LOGGERS.logging import initialize_logging
#from Hate_classification.ATTRIBUTES.attributes_entity import NormalizeDataAttributes
import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
import os
from nltk.tokenize import word_tokenize
nltk.download('punkt')  # Download necessary resources





class clean_data(ABC):
    
    @abstractmethod
    def preprocess_data(self,data:pd.DataFrame):

        pass


class DropColumns(clean_data):
    def __init__(self,data,col_to_drop:list) -> pd.DataFrame:
       self.data=data
       self.col_to_drop=col_to_drop

    def preprocess_data(self):
       logger=initialize_logging('info')
       try:
            logger.info('initializing the dropping of the columns')

            # Check and logger available columns
            logger.info(f"Columns available in DataFrame: {list(self.data.columns)}")
            data= self.data.drop(self.col_to_drop,axis=1)
            logger.info('successfully dropped the columns')
            print(data.head())
            return  data
       except Exception as e:
           logger.error(CustomExcecptionError(e,'there was an error dropping the columns'))
           print(CustomExcecptionError(e,'there was an error dropping the columns'))
    
    

class NormalizeData(clean_data) : 
    def __init__(self,data):
        self.data=data
        #self.data=NormalizeDataAttributes().data
        #self.logger=NormalizeDataAttributes().logging
        self.logger=initialize_logging('info')
        self.stopwords=set(stopwords.words('english'))  # Load English stopwords
        #self.stopwords=NormalizeDataAttributes().stopwords
        self.x_col='tweet'
        #elf.x_col=NormalizeDataAttributes().x_col
        
        

    def preprocess_data(self):
        try:
            self.lower_case()
            self.drop_punctuations()
            self.drop_stopwords()
            self.store_preprocessed_data()


        except Exception as e:
            self.logger.error(CustomExcecptionError(e,'there was an error while perfoming the normalization steps'))
            print(CustomExcecptionError(e,'there was an error while perfoming the normalization steps'))
            
            

    def lower_case(self):
        try:
            if isinstance(self.data, pd.DataFrame):
                # Ensure x_col is a valid column in the DataFrame
                if self.x_col in self.data.columns:
                    # Apply lowercase transformation to the specified column
                    self.data[self.x_col] = self.data[self.x_col].apply(lambda x: x.lower() if isinstance(x, str) else x)
                    self.logger.info('Successfully applied the lowercase transformation to the column: ' + self.x_col)
                    print("================================================================")
                    print(f'this is after  lower case {self.data.head()}')
                    return self.data
                else:
                    raise KeyError(f"Column '{self.x_col}' not found in the DataFrame")
            else:
                raise TypeError("Data provided is not a valid DataFrame")
        except Exception as e:
            self.logger.info(CustomExcecptionError(e, "Error applying lowercase transformation to {self.x_col}"))
            print(CustomExcecptionError(e, f"Error applying lowercase transformation to {self.x_col}"))

        

    def drop_punctuations(self)->pd.DataFrame:
        if isinstance(self.data, pd.DataFrame):
            try: 
                    self.logger.info('started the drop_punctuations')
                   # to   Ensure we're working with the column as a string, not object so that we dont get the error 'str' object has no attribute 'str' has occurred in module: AttributeError, line: 88, file: C:\Users\User\Desktop\nlp_text_class\Hate_classification\COMPONENTS\data_processing.py
                    self.data[self.x_col] = self.data[self.x_col].astype(str)

                    # Remove punctuation from the specified column
                    self.data[self.x_col] = self.data[self.x_col].str.replace(r'[^\w\s]', '', regex=True)

                    # Remove URLs from the specified column
                    self.data[self.x_col] = self.data[self.x_col].str.replace(r'http\S+|www\S+|https\S+', '', regex=True)

                    # Remove extra whitespace
                    self.data[self.x_col] = self.data[self.x_col].str.replace(r'\s+', ' ', regex=True).str.strip()

                    self.logger.info('Successfully dropped punctuations and URLs')
                    print ("-------------------------------")
                    print(self.data.head())
                    return self.data
            except Exception as e:
                self.logger.info(CustomExcecptionError(e,'error dropping punctuations and urls'))
                print(CustomExcecptionError(e,'error dropping punctuations and urls'))
        else:
            print('the  data is not a dataframe')
        
     

    
    def drop_stopwords(self) -> pd.DataFrame:
        self.logger.info('drop_stopwords has been initialized')
        if isinstance(self.data, pd.DataFrame):
        # Function to remove stopwords from a string
            def remove_stopwords(text):
                try:
                    
                        self.data[self.x_col] = self.data[self.x_col].astype(str)
                        if isinstance(text, str):
                            # Tokenize the text and filter out stopwods
                            words = text.split()
                            filtered_words = [word for word in words if word.lower() not in self.stopwords]
                            return " ".join(filtered_words)
                        else:
                            print('the text is not a string')
                        
                    
                except Exception as e:
                    self.logger.error(CustomExcecptionError(e,'could not remove the stop words from the dataframe '))
                    print(CustomExcecptionError(e,'could not remove the stop words from the dataframe '))
                      # If it's not a string, return as is  return text
        
        else :
         print('the data is not a dataframe')

            # Apply the remove_stopwords function to each column if it's of object type (text)
        self.data[self.x_col] = self.data[self.x_col].apply(lambda col: remove_stopwords(col) if self.data[self.x_col].dtype == 'object' else col)
        print()
        print("--------------------------------")
        print(self.data.head())
    
        return self.data
    
#python -m Hate_classification.loggerGERS.loggerging
    def store_preprocessed_data(self):
        # Get the current working directory
        current_dir = os.getcwd()
        
        # Define the file path to store the CSV file
        file_path = os.path.join(current_dir, 'clean_data.csv')
        
        # Save the preprocessed DataFrame to a CSV file
        try:
            self.data.to_csv(file_path, index=False)
            print(f"Preprocessed data successfully saved to {file_path}")
        except Exception as e:
            print(f"An error occurred while saving the file: {e}")
            self.logger.error(CustomExcecptionError(e,'could not save the file'))
            print(CustomExcecptionError(e,'could not save the file'))
        
        
    
    def lemmatize(self):
        pass

       
class FeatureEngineering(ABC ):
    
        
    @abstractmethod
    def preprocess_data(self, data: pd.DataFrame):
        pass


class Tokenization(FeatureEngineering ):
    def __init__(self,data:pd.DataFrame):
        self.data=data
        self.logging=initialize_logging('info')
        self.x_col='tweet'

    def tokenize_into_words(self,text):
        if isinstance(self.data,pd.DataFrame):
            self.data[self.x_col] = self.data[self.x_col].astype(str)
            def tokens(text):
             if isinstance(text,str) :
            
                try:
                    token=word_tokenize(text)
                    self.logging.info('tokenized_into_words successfully')
                    return token
                except Exception as e:
                    self.logging.error(CustomExcecptionError(e,'could not tokenize the text'))
                    print(CustomExcecptionError(e,'could not tokenize the text'))
             else:
                self.logging.error('the text is not a string')
        else:
           
           self.logging.error('the data is not a valaid dataframe object')

        self.data[self.x_col]=self.data[self.x_col].apply(lambda x:self.tokenize_into_words(x) if self.data[self.x_col].dtype=='object' else x)
        return  self.data


class vectorization(FeatureEngineering):
    def __init__(self,data):
        self.data=data
        self.logging=initialize_logging('info')
        self.x_col='tweet'

    def embedding_vectorization(self,text):
        pass
       

 
        
     


  