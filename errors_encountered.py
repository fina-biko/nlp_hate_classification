'''The issue you're encountering with not creating the files docker file downwads  is likely related to how the os.path.split() function handles file paths and the logic that follows for creating directories and files. When you include files like Dockerfile, setup.py, etc., which are intended to be created at the root level (i.e., without any directories), os.path.split() returns an empty string for the directory name. This may cause issues in the directory creation logic.

Why the Error Occurs:
os.path.split(path):
This function splits the path into a directory (folder_name) and a file (file_name).
For paths like "Dockerfile", os.path.split("Dockerfile") returns ('', 'Dockerfile'), meaning folder_name is an empty string.
Directory Creation Logic:
The script attempts to create directories only when folder_name is not empty. This works well for files inside directories but fails when dealing with root-level files like Dockerfile or setup.py.


Solution:
We need to ensure that the script correctly handles root-level files. Specifically, it should skip directory creation for such files but still proceed to file creation.
Ensuring Proper File Creation:
we just do  if folder_name which is same as if folder_name !='':

error associated with this command   below
logger=logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


Traceback (most recent call last):
  File "C:\Users\User\Desktop\/nlp_text_class\Template.py", line 44, in <module>
    logger.info(f"error in Created file and folders : {folder_name}")
    ^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'info'

The error you're encountering is due to an incorrect use of the logging module. Specifically, the logging.basicConfig function doesn't return a logger object; instead, it configures the root logger. As a result, when you attempt to call logger.info(...), you're actually calling info() on a NoneType object because logger is not a logger object.

Solution
You should create a logger object explicitly using logging.getLogger() after configuring it with logging.basicConfig. Here's how you can modify your script to fix the issue:
'''


#SETUP AND REQUIREMENTS
'''Issues and Fixes:
Format of requirements.txt:

Ensure that the requirements.txt file does not have any trailing commas or invalid entries. For example, setuptools, and -e . should not have trailing 
commas or be improperly formatted.
Handling -e .:

The -e . entry in requirements.txt is used for editable installs and should be handled carefully. It is not required to be in the install_requires
 list when using setup.py directly. The -e . entry should be handled separately if you want to include local development dependencies.
 If you need to include the local package (-e .) in development, consider installing it separately using pip in editable mode: as follows: 
 pip install -e .
'''

#logging, importing the customexception into logging. module
'''3. Run Your Script Correctly

When running a script that imports modules from your package, you should run the script from the parent directory of Hate_classification (i.e., the directory that contains Hate_classification). Here’s how you should do it:

Navigate to the Parent Directory:cd C:\Users\User\Desktop\/nlp_text_class
Run Your Script Using the -m Flag:

This allows Python to correctly resolve module imports relative to the package structure: 

'''
#python -m Hate_classification.LOGGERS.logging
#Explanation: this worked

'''
-m flag tells Python to run a module as a script.
Hate_classification.LOGGERS.logging specifies the module path.
'''


'''

#the custom exceeption not printing the message well in the logging module dividion by zero example, actually seeems like custom exception  has been ignored
'''
'''
here was the error 
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\User\Desktop\/nlp_text_class\Hate_classification\LOGGERS\logging.py", line 6, in <module>
    result = x / y
             ~~^~~
ZeroDivisionError: division by zero
but corrected by 
added the def__str__ since i had not put it
specifying the error is of type exception


'''

## data processing methods 
'''
When apply() is used on a DataFrame:
It applies the function to each column (the default, axis=0).
If you want to apply it to each row instead, you would specify axis=1.
'''

## data preprprocessing methods
'''def drop_punctuations(self)->pd.DataFrame:
        self.data= self.data.apply(lambda col: col.str.str.replace(r'[^\w\s]', '', regex=True))
        self.data= self.data.apply(lambda col: col.str.replace(r'http\S+|www\S+|https\S+', '', regex=True))
        self.data= self.data.apply(lambda col: col.str.replace(r'\d+', '', regex=True))
        self.data= self.data.apply(lambda col: col.str.replace(r'\s+', ' ', regex=True))
        return self.data
     
in the code abbove, if I call the function will it apply the steps by default according to how they are arranged?yes,Yes, Python executes the code in functions line by
 line, in the order in which they are written, 

'''

# knowing how to pass data that relies on previous methods
'''
In this scenario, where you have multiple methods that rely on data from previously executed methods, it is generally a better practice to define
 data as an attribute in the __init__ method.
Shared State: self.data holds the shared state of the data. Each method modifies self.data directly, so by the time the next method is executed, 
it works on the updated data.
Sequential Processing: As your methods are executed in sequence (as seen in process_pipeline()), they build on each other. The self.data is
 updated by each method and passed along naturally without the need for manually passing the data between methods.
'''

##in defining dataclass to store attirbutes and yaml file to store input to the attributes how to map them before feeding the classes that used dataclass to store attributed
#on thir behalf
''' 
so  it measn if we have used a dataclas and a yaml file to store the input, we have to match the dataclass attributes to the yaml file, 
then now feed the result to the classes that used dataclass attributes .
1. YAML File for Configuration:
The YAML file stores the input values (parameters like column names, stopwords, etc.) that control your data processing pipeline. This keeps your code 
clean and flexible by allowing you to change configurations without modifying the code.

2. Dataclass for Structure:
The dataclass is used to structure and hold the configuration values in a more manageable way. It acts as a container for all the required attributes, 
making it easy to pass them around to different components of your pipeline.

3. Mapping YAML to Dataclass:
You read the YAML configuration, and then map the values from the YAML file to the respective attributes in the dataclass. This ensures that the 
dataclass attributes match the values defined in the YAML file.
config = reading_yaml_file()  # Load the YAML configuration

# Populate the dataclass with values from the YAML file,right side is the dataclass attributes and theright side is the yaml values for the attributes
config_attributes = NormalizeDataAttributes(
    data=data,  # Your dataframe
    x_col=config['Data_processing']['x_col'],
    stopwords=set(config['Data_processing']['stopwords']),
    col_to_drop=config['Data_processing']['cols_to_drop']
)


4. Passing Dataclass to Classes:
Once the dataclass is populated with the configuration values, you can pass the dataclass object to the various classes in your pipeline that require it.
 The classes will now have access to the configuration values via the dataclass.
 # Pass the dataclass to the DropColumns class (which uses these attributes)
data = DropColumns(config=config_attributes).preprocess_data()

Good question! When you pass the config_attributes object (which is an instance of your dataclass) to the DropColumns class, it contains all the necessary data (data, x_col, stopwords, col_to_drop). The class itself determines which specific attributes from config_attributes are relevant to its own operation.

Here’s how it works in more detail:

How Does It Know Which Attribute to Use?
When you provide config=config_attributes to the DropColumns class, you control which attributes are accessed based on how the class is designed. 
In the DropColumns class, you only care about the col_to_drop attribute because this class is designed to drop columns.

The class accesses col_to_drop specifically, and not other attributes like x_col or stopwords, because in its preprocess_data method, 
it references only config.col_to_drop.

'''
#tokenization and storing the tokenized data in csv
'''
Since the tokenize_into_words() method is modifying self.config.data in place (i.e., directly updating the DataFrame stored in self.config.data), there's no need to explicitly return the tokenized data and pass it to the store_preprocessed_data() method. By the time you call store_preprocessed_data(), self.config.data already contains the tokenized data.

Here’s the summary of the workflow:

tokenize_into_words() modifies self.config.data by applying tokenization to the specified column (x_col).
store_preprocessed_data() accesses the updated self.config.data, which already contains the tokenized data, and stores it in a CSV file.
Since you're directly modifying self.config.data, there's no need to return the tokenized data from tokenize_into_words() and then pass it to 
store_preprocessed_data(). The flow works as intended.

This is how it works whenever a method uses the self.data, and returns the self.data, sos any other method that uses the self.data will get the data
 already updated data, so  no need to pass the data as an argument as in method(data) but rather just do method(self.data) adn it will  get the data that
   was modified  stored back after the methods that were called earlier  used it and returned it.
 the previous method mod
so each method only needs to call the self.data  in its implementation, then now call the methods without passing any data to the method
 def preprocess_data(self):
        try:
            self.lower_case()
            self.drop_punctuations()
            self.drop_stopwords()
            self.store_preprocessed_data()'''
#knowing how to pass data that relies on previous methods, same as previous 
'''
In this scenario, where you have multiple methods that rely on data from previously executed methods, it is generally a better practice to define
 data as an attribute in the __init__ method.
Shared State: self.data holds the shared state of the data. Each method modifies self.data directly, so by the time the next method is executed, 
it works on the updated data.
Sequential Processing: As your methods are executed in sequence (as seen in process_pipeline()), they build on each other. The self.data is
 updated by each method and passed along naturally without the need for manually passing the data between methods.
'''

#in using the embedding layer to vectorize the integers generated by the text to sequence
# the output of the text to sequence is a string of integers as  this: "8047,15,3080,12697,1196,427,37,28,5,142,0,..." in the tweet column
# so The input for the embedding layer requires numerical values, not strings. By transforming the string of comma-separated values into a 
# list of integers, we can then feed the list of integers into the mebedded layer
# so we do
# sequences = self.config.data[col_to_vectorize].apply(lambda x: list(map(int, x.split(','))))

#now, the sequences variable contains a list of lists, where each inner list represents the integer values of the corresponding tweet.
# self.config.data[col_to_vectorize]:
'''
This accesses a specific column in your DataFrame (self.config.data) that contains string representations of comma-separated values. Each entry in this column appears like this: "8047,15,3080,12697,1196,427,37,28,5,142,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0".
.apply(...):

The apply() function is a pandas method that allows you to apply a function to each element of the Series (the column you selected). Here, you are applying a lambda function to every element (each string) in the column.
lambda x: ...:

This defines an anonymous function (a lambda function) that takes a single argument, x. In this context, x represents each individual entry (string) from the selected column.
x.split(','):

For each entry x, this method splits the string at each comma, resulting in a list of string values. For example:
Input: "8047,15,3080,12697,1196,427,37,28,5,142,0,..."
Output: ["8047", "15", "3080", "12697", "1196", "427", ...].
map(int, x.split(',')):

The map() function applies the int function to each element of the list produced by x.split(','). This converts each string in the list into an integer. So the output
 would now be a map object that contains integers instead of strings:
Output: [8047, 15, 3080, 12697, 1196, 427, ...].
list(...):

Finally, the list() function converts the map object into a regular Python list, making it easier to work with. 
'''

Alternative Method Using Environment Variables
To avoid exposing your token in the notebook, you can set it as an environment variable. Here’s how:

Set the Environment Variable:

python
Copy code
import os
os.environ['GITHUB_TOKEN'] = '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'
Push Using the Environment Variable:

Then use the variable in your push command:

python
Copy code
!git push https://fina-biko:$GITHUB_TOKEN@github.com/fina-biko/nlp_hate_classification.












