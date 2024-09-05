import os
import logging
from pathlib import Path

ROOT_FOLDER="Hate_classification"

list_of_files=[
    f"{ROOT_FOLDER}/__init__.py",
    f"{ROOT_FOLDER}/ARTIFACTS/",
    f"{ROOT_FOLDER}/COMPONENTS/__init__.py",
    f"{ROOT_FOLDER}/COMPONENTS/data_ingestion.py",
    f"{ROOT_FOLDER}/COMPONENTS/data_processing.py",
    f"{ROOT_FOLDER}/COMPONENTS/model_training.py",
    f"{ROOT_FOLDER}/COMPONENTS/model_evaluation.py",
    f"{ROOT_FOLDER}/COMPONENTS/model_inference.py",
    f"{ROOT_FOLDER}/COMPONENTS/data_visualization.py",
    f"{ROOT_FOLDER}/CONFIGURATION/__init__.py",
    f"{ROOT_FOLDER}/EXCEPTIONS/__init__.py",
    f"{ROOT_FOLDER}/EXCEPTIONS/exceptions.py",
    f"{ROOT_FOLDER}/EXCEPTIONS/exceptions.py",
    f"{ROOT_FOLDER}/CONSTANTS/__init__.py",
    f"{ROOT_FOLDER}/CONSTANTS/constants.py",
    f"{ROOT_FOLDER}/LOGGERS/__init__.py",
    f"{ROOT_FOLDER}/LOGGERS/logging.py",
    f"{ROOT_FOLDER}/PIPELINE/__init__.py",
    f"{ROOT_FOLDER}/UTILS/__init__.py",
    f"{ROOT_FOLDER}/UTILS/utility.py",
    f"{ROOT_FOLDER}/ML/__init__.py",
    f"Dockerfile",
    f"setup.py",
    f"main.py",
    f"requirements.txt",
    f"README.md",
    f"LICENSE"

]


# Configure the logger
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)# or use logging if you dont want this get loger

# Create folders and files recursively
try:
    for filepath in list_of_files:
        path=Path(filepath)
        folder_name,file_name=os.path.split(path)
        if folder_name != '' :
            os.makedirs(folder_name,exist_ok=True)
            logger.info(f"Created {folder_name} successfully")
        else:
            logger.info(f"error in Creating folder : {folder_name}")

        # Handle root level files
        if not os.path.exists(file_name):
            with open(filepath, "w"):
                pass
            logging.info(f"Created file: {filepath}")
        else:
           logging.info(f"File already exists: {filepath}")
except Exception as e:
    #logging.error(f"Error in creating folder and file: {filepath}. Exception: {str(e)}")
   
   logger.info(f"Error in creating folder and file: {filepath}. Exception: {str(e)}")



