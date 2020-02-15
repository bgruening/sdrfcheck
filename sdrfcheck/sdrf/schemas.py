
from pandas_schema import Column, Schema
from pandas_schema.validation import LeadingWhitespaceValidation, TrailingWhitespaceValidation, CanConvertValidation, MatchesPatternValidation, InRangeValidation, InListValidation

human_schema = Schema([
    Column('Source Name', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
    Column('Characteristics[organism part]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
    Column('Characteristics[disease]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()])
])