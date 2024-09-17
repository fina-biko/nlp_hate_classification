from dataclasses import dataclass
from pathlib import Path
import pandas as pd
from Hate_classification.EXCEPTIONS.exceptions import  CustomExcecptionError
from Hate_classification.LOGGERS.logging import initialize_logging
from nltk.corpus import stopwords
@dataclass
class NormalizeDataAttributes(frozen=True):
     data: pd
     logging =initialize_logging('info')
     x_col ='tweet'
     stopwords=set(stopwords.words('english'))