from dataclasses import dataclass
from pathlib import Path
import pandas as pd
from Hate_classification.EXCEPTIONS.exceptions import  CustomExcecptionError
from Hate_classification.LOGGERS.logging import initialize_logging
from nltk.corpus import stopwords
from dataclasses import dataclass
import pandas as pd
from nltk.corpus import stopwords

@dataclass()
class NormalizeDataAttributes:
    data: pd.DataFrame  ## Input data, to be set in the pipeline
    x_col: str  # Column name for features, coming from YAML
    cols_to_drop: list # Columns to drop, this will come from the YAML file
    stopwords: set = frozenset(stopwords.words('english'))  # Set of stopwords# Stopwords set (could also come from YAML or another source)
   

    # You can remove the logging from here, as it should be handled in methods

