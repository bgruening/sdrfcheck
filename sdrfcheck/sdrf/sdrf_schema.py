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

        # Check minimum number of columns
        if check_minimum_columns(panda_sdrf, self._min_columns):
            error_message = 'The number of columns in the SDRF ({}) is smaller than the number of mandatory fields ({})'.format(len(panda_sdrf.get_sdrf_columns()), self._min_columns)
            errors.append(LogicError(error_message, error_type=logging.WARN))

        # Check the mandatory fields
        error_mandatory = self.validate_mandatory_columns(panda_sdrf)
        if error_mandatory is not None:
            errors.append(error_mandatory)
        return errors

    def validate_mandatory_columns(self, panda_sdrf):
        error_mandatory = []
        for column in self.columns:
            if(column._optional == False and column.name not in panda_sdrf.get_sdrf_columns()):
                error_mandatory.append(column.name)
        if len(error_mandatory):
            error_message = 'The following columns are mandatory and not present in the SDRF: {}'.format(",".join(error_mandatory))
            return LogicError(error_message, error_type=logging.ERROR)
        return None


minimum_schema = SDRFSchema([
    SDRFColumn('source name', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()], allow_empty=True,
               optional_type=False),
    SDRFColumn('characteristics[organism part]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()],
               allow_empty=True, optional_type=False),
    SDRFColumn('characteristics[disease]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()],
               allow_empty=True, optional_type=False),
    SDRFColumn('characteristics[organism]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()],
               allow_empty=True, optional_type=False),
    SDRFColumn('characteristics[cell type]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()],
               allow_empty=True, optional_type=False),
    SDRFColumn('comment[data file]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()], allow_empty=True,
               optional_type=False),
    SDRFColumn('comment[fraction identifier]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()],
               allow_empty=True, optional_type=False)],
    min_columns=7)

human_schema = SDRFSchema([
    Column('Source Name', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
    Column('Characteristics[organism part]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
    Column('Characteristics[disease]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()])
])
