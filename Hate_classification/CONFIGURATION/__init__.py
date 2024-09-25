from Hate_classification.COMPONENTS.data_processing import DropColumns
from Hate_classification.COMPONENTS.data_processing import NormalizeData,Tokenization,TokensToSequence
import pandas as pd
from Hate_classification.LOGGERS.logging import initialize_logging
from Hate_classification.EXCEPTIONS.exceptions import CustomExcecptionError
from Hate_classification.ATTRIBUTES.attributes_entity import NormalizeDataAttributes,FeatureEngineerringAttributes
import os
import pandas as pd
import yaml

'''
from Hate_classification.PIPELINE.ingestion_pipeline_steps import data_ingestion_pipeline
from Hate_classification.COMMON_METHODS import reading_yaml_file


 # Populate NormalizeDataAttributes dataclass  with values from the config
    config_attributes_processing = NormalizeDataAttributes(
        data=data,
        x_col=config['Data_processing']['x_col'],
        
        #stopwords=set(config['Data_processing']['stopwords']),
        cols_to_drop=config['Data_processing']['cols_to_drop']
    )'''