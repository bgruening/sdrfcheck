import logging
import typing
from typing import Any

from pandas_schema import Column, Schema, ValidationWarning
from pandas_schema.validation import LeadingWhitespaceValidation, TrailingWhitespaceValidation

from sdrfcheck.sdrf import sdrf
from sdrfcheck.sdrf.exceptions import LogicError

def check_minimum_columns(panda_sdrf= None, minimun_columns:int = 0):
    return len(panda_sdrf.get_sdrf_columns()) < minimun_columns

class SDRFColumn(Column):

    def __init__(self, name: str, validations: typing.Iterable['validation._BaseValidation'] = [], allow_empty=False,
                 optional_type=True):
        super().__init__(name, validations, allow_empty)
        self._optional = optional_type


class SDRFSchema(Schema):

    def __init__(self, columns: typing.Iterable[SDRFColumn], ordered: bool = False, min_columns: int = 0):
        super().__init__(columns, ordered)
        self._min_columns = min_columns

    def __new__(cls, ordered: bool = False, min_columns: int = 0) -> Any:
        obj = super().__new__(cls)
        obj._min_columns = min_columns
        return obj

    def validate(self, panda_sdrf: sdrf = None) -> typing.List[LogicError]:
        errors = []
        if check_minimum_columns(panda_sdrf, self._min_columns):
            error_message = 'The number of columns in the SDRF {} is smaller than the number of minimum, columns {}'.format(len(panda_sdrf.get_sdrf_columns()), self._min_columns)
            errors.append(LogicError(error_message, error_type=logging.WARN))
        return errors


minimum_schema = SDRFSchema([
    SDRFColumn('Source Name', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()], allow_empty=True,
               optional_type=False),
    SDRFColumn('Characteristics[organism part]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()],
               allow_empty=True, optional_type=False),
    SDRFColumn('Characteristics[disease]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()],
               allow_empty=True, optional_type=False),
    SDRFColumn('Characteristics[organism]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()],
               allow_empty=True, optional_type=False),
    SDRFColumn('Characteristics[cell type]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()],
               allow_empty=True, optional_type=False),
    SDRFColumn('Comment [data file]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()], allow_empty=True,
               optional_type=False),
    SDRFColumn('Comment [fraction identifier]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()],
               allow_empty=True, optional_type=False)],
    min_columns=59)

human_schema = SDRFSchema([
    Column('Source Name', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
    Column('Characteristics[organism part]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
    Column('Characteristics[disease]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()])
])
