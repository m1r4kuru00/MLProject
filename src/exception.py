import sys
import logging


logging.basicConfig(level=logging.INFO)

def error_message_detail(error, error_detail:sys):
    """
    A function to generate an error message detail based on the error and error_detail parameters.
    :param error: The error that occurred.
    :param error_detail: An object containing details about the error.
    :return: The error message containing the file name, line number, and error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        """
        Initialize the error message and error detail.
        :param error_message: The error message to be initialized.
        :param error_detail: The error detail to be initialized.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    def __str__(self):
        """
        Return the error message as a string representation of the object.
        """
        return self.error_message

if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.error("Divide by zero error")
        raise CustomException(e, sys)
