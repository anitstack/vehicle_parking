from datetime import datetime
import logging
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class CommandNotFoundException(Exception):
    """Exception raised for not existing command.

    Attributes:
        command -- the command for which we got exception
    """
    def __init__(self, command):
        self.command = command
        super().__init__()

    def __str__(self):
        return '{} not found \nFor help type "python app.py --help"'.format(self.command)


class InvalidCommandException(Exception):
    """Exception raised for invalid command.

    Attributes:
        command -- the command for which we got exception
    """
    def __init__(self, command):
        self.command = command
        super().__init__()

    def __str__(self):
        return 'Invalid value in command - {} \nFor help type "python app.py --help"'.format(self.command)

class StandardError(Error):
    """Exception raised for errors in the input.

    Attributes:
        code -- the error code
        message -- explanation of the error
    """

    def __init__(self, code, message):
        self.code = code
        self.message = message
