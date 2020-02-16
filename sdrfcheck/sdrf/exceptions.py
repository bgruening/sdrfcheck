import logging
from enum import IntEnum


class AppException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


__all__ = ['LogicError']


class LogicError(IntEnum):
    """
    This class process all the errors presented in the SDRF
    """

    def __new__(cls, code, phrase, description='', type=logging.WARN):
        obj = int.__new__(cls, code)
        obj._value_ = code
        obj._phrase_ = phrase
        obj._description_ = description
        obj._type_ = type
        return obj

    def get_code(self):
        return self._value_

    def get_phrase(self) -> str:
        return self._phrase_

    @staticmethod
    def get_type(error_type: int) -> logging:
        return logging.getLevelName(error_type)

    NUMBER_COLUMNS = 100, 'Number of columns', 'The number of columns', logging.WARN

    @staticmethod
    def process_errors(errors):
        error_list = []
        for error in errors:
            if "Invalid number of columns" in error.message:
                error_list.append(LogicError.NUMBER_COLUMNS)
        return error_list

    def __str__(self) -> str:
        return "{ " + self._phrase_ + " }" + " -- " + "{ " + self.get_type(self._type_) + " }"


class AppConfigException(AppException):
    def __init__(self, value):
        super(AppConfigException, self).__init__(value)


class ConfigManagerException(Exception):
    def __init__(self, value):
        Exception.__init__(self)
        self.value = value

    def __str__(self):
        return repr(self.value)
