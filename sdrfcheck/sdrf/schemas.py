import typing

from pandas_schema import Column, Schema, schema
from pandas_schema.validation import LeadingWhitespaceValidation, TrailingWhitespaceValidation

from sdrfcheck.sdrf import sdrf
from sdrfcheck.sdrf.exceptions import LogicError


class SDRFSchema(Schema):

    def __init__(self, columns: typing.Iterable[Column], ordered: bool = False, min_columns: int = 0):
        super().__init__(columns, ordered)
        self._min_columns = min_columns

    def validateSDRF(self, panda_sdrf: sdrf = None) -> typing.List[LogicError]:
        errors = self.validate(panda_sdrf)
        return LogicError.process_errors(errors)


minimum_schema = SDRFSchema([
    Column('Source Name', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
    Column('Characteristics[organism part]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
    Column('Characteristics[disease]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
    Column('Characteristics[organism]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
    Column('Characteristics[cell type]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
    Column('Comment [data file]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
    Column('Comment [fraction identifier]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
    Column('Comment [1]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()])
])

human_schema = SDRFSchema([
    Column('Source Name', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
    Column('Characteristics[organism part]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
    Column('Characteristics[disease]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()])
])
