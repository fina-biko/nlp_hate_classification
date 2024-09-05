import sys
import os
from time import time, strftime, gmtime
from Hate_classification.EXCEPTIONS.exceptions import CustomExcecptionError
import logging
parent_folder='Hate_classification/LOGGERS'
# The filename will be based on the current time
filename = os.path.join(parent_folder, f"log_{strftime('%Y%m%d_%H%M%S', gmtime())}.log")

def initialize_logging(level):
    logger=logging.getLogger(__name__)
    
    # Initialize log_level with a default value
    log_level = logging.INFO 
    # Set the log level based on the user's choice
    if level is not None:
        if level.upper() == 'INFO':
            log_level = logging.INFO
        elif level.upper() == 'DEBUG':
            log_level = logging.DEBUG
    
    logger.setLevel(log_level)

    #create the formatter
    format=logging.Formatter('%(filename)s----%(module)s---%(asctime)s---%(levelname)s---%(funcName)s---%(name)s---%(message)s')
    #name will bring up the name of the module in which we have used this  logging function, 
    #The %(name)s field in your log formatter will show the value captured by logging.getLogger(__name__).
    #%(name)s: Displays the name captured by logging.getLogger(__name__), which should match the module name, e.g., constants.
    #module will be the name of the module currently using this logging function, same as the 'name' above 
    #fuction name will be the name of the function in which we have used the logging
    #filename will be the name of the file same as (module) in its case it brings  constants.py while (module) willbring constants

    #create the handler
    handler=logging.FileHandler(filename)
    #add the formatter to the handler
    handler.setFormatter(format)
    #add the handler to the logger
    logger.addHandler(handler)
    return logger





'''
is testing for the exception
def try_exception():
    try:
        x = 10
        y = 0
        result = x / y
    except ZeroDivisionError as e:
        # Capture original exception details
        error_message = "this  error occurred while dividing."
        # Raise custom exception with additional message
        raise CustomExcecptionError(e, error_message)

try:
    try_exception()
except CustomExcecptionError as e:
    print(e)
   '''

'''
#is testing the logger
def try_exception():
    loggerm=initialize_logging('INFO')
    try:
        x = 10
        y = 0
        result = x / y
        loggerm.info('division successful')
    except ZeroDivisionError as e:
        # Capture original exception details
        error_message = "this  error occurred while dividing."
        # Raise custom exception with additional message
        loggerm.info('division by zero failed')
        raise CustomExcecptionError(e, error_message)
    

try:
    try_exception()
except CustomExcecptionError as e:
    print(e)
    '''