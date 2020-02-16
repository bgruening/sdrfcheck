
from pandas_schema import Column, Schema
from pandas_schema.validation import LeadingWhitespaceValidation, TrailingWhitespaceValidation

minimum_schema = Schema([
    Column('Source Name', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
    Column('Characteristics[organism part]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
    Column('Characteristics[disease]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
    Column('Characteristics[organism]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
    Column('Characteristics[cell type]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
    Column('Comment [data file]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
    Column('Comment [fraction identifier]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
    Column('Comment [1]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()])
])


human_schema = Schema([
    Column('Source Name', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
    Column('Characteristics[organism part]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
    Column('Characteristics[disease]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()])
])