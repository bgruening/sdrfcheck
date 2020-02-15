import logging
from enum import IntEnum
from http import HTTPStatus
from logging import Logger


class AppException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class LogicError:
    """
    This class process all the errors presented in the SDRF
    """

    def __init__(self, code: int, phrase: str, description: str, type: logging) -> None:
        self._code_ = code
        self._phrase_ = phrase
        self._description_ = description
        self._type_ = type

    def get_code(self) -> int:
        return self._value_

    def get_phrase(self) -> str:
        return self._phrase_

    def get_type(self) -> str:
        return logging.getLevelName(self._type_)

    @staticmethod
    def process_errors(errors):
        error_list = []
        for error in errors:
            if ("Invalid number of columns" in error.message):
                error_list.append(NUMBER_COLUMNS)
        return error_list

    def __str__(self) -> str:
         return "{ " + self.get_phrase() + " }" + " -- " + "{ " + self.get_type() + " }"


NUMBER_COLUMNS = LogicError(100, 'Number of columns', 'The number of columns', logging.WARN)


class AppConfigException(AppException):
    def __init__(self, value):
        super(AppConfigException, self).__init__(value)


class ConfigManagerException(Exception):
    def __init__(self, value):
        Exception.__init__(self)
        self.value = value

    def __str__(self):
        return repr(self.value)
