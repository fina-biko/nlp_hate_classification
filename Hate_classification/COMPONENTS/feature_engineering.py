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
import tensorflow as tf
from nltk.tokenize import word_tokenize
nltk.download('punkt')  # Download necessary resources


#tokens to integers
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.layers import Embedding
from tensorflow.keras.preprocessing.sequence import pad_sequences


class FeatureEngineering(ABC ):
    
        
    @abstractmethod
    def preprocess_data(self, data: pd.DataFrame):
        pass



class Tokenization(FeatureEngineering ):
    '''Tokenizes the data
    stores the tokenized dataframe into a csv file'''
    def __init__(self,config:NormalizeDataAttributes):
        #self.self.config.data=self.config.data
        self.logging=initialize_logging('info')
        self.config=config
        
       # self.x_col='tweet'

    def preprocess_data(self):
        self.tokenize_into_words()
        return self.store_preprocessed_data()  # Return the result from the last method
    


    def tokenize_into_words(self):
       if isinstance(self.config.data, pd.DataFrame):
        self.config.data[self.config.x_col] = self.config.data[self.config.x_col].astype(str)
 
        # Define the inner function tokens() correctly
        def tokens(text):
            if isinstance(text, str):
                try:
                    token = word_tokenize(text)
                    self.logging.info('tokenized_into_words successfully')
                    return token
                except Exception as e:
                    self.logging.error(CustomExcecptionError(e, 'could not tokenize the text'))
                    print(CustomExcecptionError(e, 'could not tokenize the text'))
            else:
                self.logging.error('the text is not a string')

        # Apply the tokens function to the column
        self.config.data[self.config.x_col] = self.config.data[self.config.x_col].apply(
            lambda x: tokens(x) if self.config.data[self.config.x_col].dtype == 'object' else x
        )
        print('----------------------The final tokenized data------------------------')
       
        return self.config.data

       else:
        self.logging.error('the self.config.data is not a valid self.config.dataframe object')

            
#python -m Hate_classification.loggerGERS.loggerging
    def store_preprocessed_data(self):
        # Get the current working directory
        #current_dir = os.getcwd()
        
        # Define the file path to store the CSV file
        # Define the file path to store the CSV file
        file_path = os.path.join('Hate_classification', 'ARTIFACTS', 'Tokeninized_data.csv')
        #file_path = os.path.join(current_dir, 'clean_self.config.data.csv')
        
        # Save the preprocessed self.config.dataFrame to a CSV file
        try:
            print(type(self.config.data))
            self.config.data.to_csv(file_path, index=False)
            print(f"Tokenized {self.config.data} successfully saved to {file_path}")
            print(f" finished the tokenization steps successfully ")
            return self.config.data
        
        except Exception as e:
            print(f"An error occurred while saving the file: {e}")
            self.logging.error(CustomExcecptionError(e,'could not save the file'))
            print(CustomExcecptionError(e,'could not save the file'))
        
        


class TokensToSequence(FeatureEngineering):
   def __init__(self,config=FeatureEngineerringAttributes):
       self.config = config
       self.tokenizer_object=Tokenizer()
       self.logging=initialize_logging('info')

   def preprocess_data(self):
       self.texts_sequences()
       self.padding()
       return self.store_textstosequences()  # Return the result from the last method
       

   def texts_sequences(self):
        self.col_name =self.config.data[self.config.x_col]
        

        self.logging.info('fittinf the tokenizer to text has started')
        self.tokenizer_object.fit_on_texts(self.col_name)
        print('starting the text to sequence processing')
        self.sequences=self.tokenizer_object.texts_to_sequences(self.col_name)
        self.config.data[self.config.x_col]=self.sequences
        self.logging.info('fittinf the tokenizer  and text to sequence  has finished successfully')
        print('finished the text to sequence processing,next should be padding')
        return self.config.data
 

    
   def padding(self):
        
        max_length=self.config.max_length
        col_name=self.config.data[self.config.x_col]
        self.logging.info('padding has started')
        print('padding started')
        self.padded_sequences=pad_sequences(col_name,maxlen=max_length,padding='post',truncating='post')
        self.config.data[self.config.x_col]=self.padded_sequences.tolist()

        # Convert each row in `self.padded_sequences` to a string format
        self.config.data[self.config.x_col] = self.config.data[self.config.x_col].apply(lambda x: ','.join(map(str, x)))
        self.logging.info('padding is done successfully,next is saving into a file')
        print('padding finished')
        return self.config.data
       
   def store_textstosequences(self):
        file_path = os.path.join('Hate_classification', 'ARTIFACTS', 'text_to_sequence.csv')
        try:
            self.config.data.to_csv(file_path, index=False)
            print(f"sequenced data  {self.config.data} successfully saved to {file_path}")
            print(f"finished the text to sequence  steps successfully ")
            print(self.config.data.head())
            return self.config.data
        
        except Exception as e:
            print(f"An error occurred while saving the file: {e}")
            self.logging.error(CustomExcecptionError(e,'could not save the file'))
            print(CustomExcecptionError(e,'could not save the text_to_sequence file'))
  

class EmbeddingAbstractClasss(ABC):
    '''

    
    aurguments:sequenced data in the form of intergers thfat is the direct return  of the tokenization class'''
    @abstractmethod
    def preprocess_data(self):
        pass

class Embedding_sequences(EmbeddingAbstractClasss):
    def __init__(self,config:FeatureEngineerringAttributes)  :
        self.config=config
        self.logging=initialize_logging('info')

    def preprocess_data(self):
        print('generating word embeddings and then storing them in a file ')
        try:
            self.generate_word_embeddings()
            print('done with generating word embeddings')
            return self.store_embedded_vector()  # Return the result from the last method
        except Exception as e:
            print('An error occurred while generating the embeddings' + str(e))
            self.logging.error(CustomExcecptionError(e))
            
    

    def generate_word_embeddings(self, x_col=None, output_dim=100):
        try:
            if x_col is not None:
                col_to_vectorize = x_col
                self.logging.info("Using the specified x col for inference mode")
            else:
                col_to_vectorize = self.config.x_col
                self.logging.info("Using the default x col for training mode")
            
            # Convert column to lists of integers
            sequences = self.config.data[col_to_vectorize].apply(lambda x: list(map(int, x.split(','))))
            sequences = np.array(sequences.tolist(), dtype=np.int32)

            # Print unique values for debugging
            unique_values = np.unique(sequences)
            print("Unique values in sequences:", unique_values)
            print("Min value:", unique_values.min())
            print("Max value:", unique_values.max())

            # Ensure input_dim is at least the maximum index + 1
            input_dim = max(unique_values.max() + 1, 50)  # Adjust as necessary
            output_dim=100

            # Create the embedding layer
            embedding_layer = Embedding(input_dim=input_dim, output_dim=output_dim)

            # Get embeddings
            embeddings = embedding_layer(sequences)

            # Average embeddings across the sequence length
            embeddings_avg = tf.reduce_mean(embeddings, axis=1).numpy()  # Shape will be (24783, 100)

            # Convert embeddings to DataFrame
            embedding_df = pd.DataFrame(embeddings_avg, columns=[f'embedding_dim_{i}' for i in range(output_dim)])

            # Concatenate the new embedding columns to the original DataFrame
            self.config.data = pd.concat([self.config.data, embedding_df], axis=1)
            return self.config.data

        except Exception as e:  
            print(CustomExcecptionError(e))
            self.logging.error(CustomExcecptionError(e))
            print('An error occurred while generating the embeddings')




    def  store_embedded_vector(self):
        filepath = os.path.join('Hate_classification', 'ARTIFACTS', 'embedded_vector.csv')
        
        
        self.logging.info('storing the embedded data')
        try:
             self.config.data.to_csv(filepath)
             print('successfully saved the embedded data  to ' + filepath) 
             return self.config.data
        except Exception as e:
            print(CustomExcecptionError(e))
        
        










'''
try:
            data=Tokenization(config_attributes_processing).preprocess_data()
            log.info('Successfully finished the tokenization')
            print('Successfully finished the tokenization')
        except Exception as e:
            log.error(CustomExcecptionError(e,'error occurred while tokenization'))
            print(CustomExcecptionError(e,'error occurred while tokenization'))

'''
    