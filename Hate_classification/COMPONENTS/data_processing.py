from abc import ABC, abstractmethod
from Hate_classification.EXCEPTIONS.exceptions import  CustomExcecptionError
from Hate_classification.LOGGERS.logging import initialize_logging
import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords


class clean_data(ABC):
    
    @abstractmethod
    def preprocess_data(self,data:pd.DataFrame):

        pass


class DropColumns(clean_data):
    def __init__(self,data,col_to_drop:list) -> pd.DataFrame:
       self.data=data
       return self.data.drop(col_to_drop)
       

    

class NormalizeData(clean_data) : 
    def __init__(self,data):
        self.data=data
        self.logging=initialize_logging('info')
        self.stopwords=set(stopwords.words('english'))  # Load English stopwords
        

        pass

    def preprocess_data(self):
        try:
            self.lower_case()
            self.drop_punctuations()
            self.drop_stopwords()
        
        except Exception as e:
            self.logging('error normalizing the data')
            raise CustomExcecptionError(e)

    def lower_case(self):
       
        try:
            self.data=self.data.apply(lambda col: col.str.lower()if self.data[col].dtype=='object' else col)
            self.logging('successfully applied the lowercase transformation to the data ')
        
        except Exception as e:
            self.logging('error applying the lowercase transformation')
            raise CustomExcecptionError(e)
        

    def drop_punctuations(self)->pd.DataFrame:
        try:
            self.logging('started the drop_punctuations')
            self.data= self.data.apply(lambda col: col.str.str.replace(r'[^\w\s]', '', regex=True))
            self.data= self.data.apply(lambda col: col.str.replace(r'http\S+|www\S+|https\S+', '', regex=True))
            self.data= self.data.apply(lambda col: col.str.replace(r'\d+', '', regex=True))
            self.data= self.data.apply(lambda col: col.str.replace(r'\s+', ' ', regex=True))
            self.logging('Successfully dropped punctuations and urls')
            return self.data
        except Exception as e:
            self.logging('error dropping punctuations and urls')
            raise CustomExcecptionError(e)
     

    
    def drop_stopwords(self) -> pd.DataFrame:
        self.logging('drop_stopwords has been initialized')
        # Function to remove stopwords from a string
        def remove_stopwords(text):
            try:
                if isinstance(text, str):
                    # Tokenize the text and filter out stopwods
                    words = text.split()
                    filtered_words = [word for word in words if word.lower() not in self.stop_words]
                    return " ".join(filtered_words)
            except Exception as e:
               raise CustomExcecptionError(e)
            return text  # If it's not a string, return as is

        # Apply the remove_stopwords function to each column if it's of object type (text)
        self.data = self.data.apply(lambda col: col.apply(remove_stopwords) if col.dtype == 'object' else col)
        return self.data

  
    
    def lemmatize(self):
        pass

        
class FetureEngineering(clean_data):
    def __init__(self,data):
        self.data=data

    def preprocess_data(self, data: pd.DataFrame):
        pass

     


    