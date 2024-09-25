
import os
import yaml
from Hate_classification.EXCEPTIONS.exceptions import  CustomExcecptionError
from Hate_classification.LOGGERS.logging import initialize_logging

def reading_yaml_file():
    log=initialize_logging('info')
    log.info('programatically constructing the yaml file path')
    try:
        yaml_file = os.path.join('Hate_classification', 'YAML_FILES', 'config.yaml')
        log.info('Done with programatically constructing the yaml file path')

        with open (yaml_file, 'r') as file:
            config=yaml.safe_load(file)
            return config
    except Exception as e:
        CustomExcecptionError(e)
        print(CustomExcecptionError(e))
