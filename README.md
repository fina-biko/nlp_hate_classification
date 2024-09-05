## THIS IS  AN OUTLINE OF THE STEPS BY STEPS WORKFKOW OF THE PROJECT FROM START TO FINISH.
NLP PROJECT PIPELINE:
DATA ACQUISITION
    -Available  data(cvs, txt,pdf)
    -other data(Database;Internet,API data, scraped data,)
    -No data(create your own data  ; use LLM to make data; issue out surveys then perform dat
    a augmentation  such as BIagram flip, BAck Translate, Add additonal  noise, replace with synonymns incase of less data)

TEXT PREPARATION
    GENERAL /BASIC PREPROCESSING
         Tokenization
         stop words removal
         stemming/ lemmatization
         remove punctuation
         convert to lower case
    CONTEXT BASED / ADVANCED PREPROCESSINg
        POS tagging
        Parsing(parsing tree)
        Coreference reduction

FEATURE ENGINEERING
MODEL TRAINING
MDOEL EVALUATION



PROJECT SETUP AND UTILITY MODULES (Flow chart of how we arrange the folders)  :
    (first)create the Project template.py that will  provide code for creating the folders , subfolders and files  according to the flowchart below instead of creating each manually
       
    
    HATE classification(root folder)
            COMPONENTS folder
                data_ingestion.py
                data transformation.py
                model trainer.py
                model_evaluation.py
                model_pusher.py
           (fifth) CONFIGURATION folder
                s3 operations.py
            CONSTANTS folder
                    artifact_entity.py
                    config_entity.py
            EXCEPTIONS folder
            LOGGER folder
            PIPELINE folder
               train_pipeline.py
               Prediction_Pipeline.py
            UTILS  folder
              main_utils.py
            ML folder
              feature
              models
        main or app.py
        jupyuter_notebook.py
        requirement.txt
        Dockerfile
        setup.py   
        .dockerIgnore 
    (second)setup the requiremnts
     cofigure GCP 
    (third)Logging 
    (fourth)Exception
    (sixth)project workflow(flowchart of the project folders)
          (sixth)project notebook experiment jupyter done in Google colab;  how we can do the project on a jupyter notebook
           Data Preprocessing---handle missing values, encode categorical values, scale numerical features
           EDA
           feature engineering--- engineering new features based on the knowledge  and insights from the EDA
           Model building ---- train and evaluate several models  to ge the best
           Model evaluation ----evaluate the trained models so as to choose the best model
        (seventh)
       Update the constants folder
       update the cofigurations folder
       update the  artifacts folder
       update the components folder
       update the pipeline folder
       update the main file or the app.py
