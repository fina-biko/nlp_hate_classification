 #we do not know the error we aare likely to get  from the modules , so we use the general custom exception that will give us details of the erro the 
# module and the line. we want to use this custom exception after we have found the error with the help of  the except() key word , meaning this custom
#  exception requires the error as its first argument, 
# so we have defined a function that will expound on this error which is the first argument and then the function will return a statement, 
# then came to the fucntion


self.message = message# optional message that user will want to write so as to printed in addition to to the error message

def __str__(self):
        return f"{self.message} - {self.error_details}"# so  this "Error: {error_value} has occured in , module: {error_type.__name__}, line: {line_number}, file: {file_name}"
        #  that is returned by the function is what will be stored in the error_details attribute
