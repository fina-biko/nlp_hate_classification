from abc import ABC, abstractmethod
from Hate_classification.EXCEPTIONS.exceptions import  CustomExcecptionError
from Hate_classification.LOGGERS.logging import initialize_logging
from Hate_classification.ATTRIBUTES.attributes_entity import NormalizeDataAttributes
from Hate_classification.ATTRIBUTES.attributes_entity import FeatureEngineerringAttributes
import pandas as pd
import numpy as np

'''The model to be used will be the deep learning models and the Traditional model , then evaluation of the models performed to determine the model that will be used for training  and evaluation of the models 
'''