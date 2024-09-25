import sys

def error_details(error: Exception) -> str:
    '''Receive the error that has occurred and return the details of the error in terms of the message, the module, and the line.'''
    error_type, error_value, error_traceback = sys.exc_info()
    file_name = error_traceback.tb_frame.f_code.co_filename
    line_number = error_traceback.tb_lineno
    return f"Error: {error_value},{error_type.__name__} ,line: {line_number},has occurred in module:  file: {file_name}"

class CustomExcecptionError(Exception):
    def __init__(self, error: Exception, message: str = None):
        super().__init__(message)
        self.message = message
        self.error_details = error_details(error)
    
    def __str__(self):
        return f"{self.message} - {self.error_details}"
