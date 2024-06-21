import sys

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name[{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super.__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message


"""
_,_,exc_tb=error_detail.exc_info():

error_detail.exc_info() is a method from the sys module that returns a tuple of three values: (type, value, traceback).
type: The type of the exception (e.g., ValueError, TypeError).
value: The exception instance itself.
traceback: A traceback object which encapsulates the call stack at the point where the exception occurred.
In the line of code you provided:

The first two values (type and value) are ignored by using the underscore _.
exc_tb is assigned the third value, which is the traceback object.

Essentially, this line extracts the traceback object from the current exception, which can be useful for logging or debugging purposes. The traceback object contains information about where the exception occurred, allowing you to trace the sequence of calls that led to the error.


exc_tb.tb_frame gets the frame object from the traceback.
f_code.co_filename retrieves the filename where the exception occurred.
"""