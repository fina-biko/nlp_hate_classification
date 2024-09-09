from abc import ABC
from abc import abstractmethod
import pandas as pd
from Hate_classification.LOGGERS.logging import initialize_logging
from Hate_classification.EXCEPTIONS.exceptions import CustomExcecptionError
from pathlib import Path
class DataIngestionStrategy(ABC):
    @abstractmethod
    def ingest_data(self, path:str):
   
        
     pass



class DataIngestion(DataIngestionStrategy):
    def __init__(self,path:str):
        self.path=Path(path)

    def ingest_data(self)->pd.DataFrame:
        logging=initialize_logging('info')
        try:
           
            logging.info("initialized Reading CSV from { self.path} ") 
            return  pd.read_csv(self.path)
        except Exception as e:
            CustomExcecptionError(e,'error reading CSV from  the path specified { self.path}' )

  
'''
if __name__ == "__main__":
    DataIngestion.ingest_data(r'C:\Users\User\Desktop\labeled_data.csv')
 '''



