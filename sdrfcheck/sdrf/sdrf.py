import pandas as pd
from pygments.lexer import default

from sdrfcheck.sdrf.exceptions import LogicError
from sdrfcheck.sdrf.sdrf_schema import human_schema, HUMAN_TEMPLATE, VERTEBRATES_TEMPLATE, \
    vertebrates_chema, DEFAULT_TEMPLATE, NON_VERTEBRATES_TEMPLATE, nonvertebrates_chema, PLANTS_TEMPLATE, plants_chema, \
    CELL_LINES_TEMPLATE, cell_lines_chema, default_schema
from ebi.ols.api.client import OlsClient


class SdrfDataFrame(pd.DataFrame):

    @property
    def _constructor(self, template):
        """
        This method is makes it so our methods return an instance
        :return:
        """
        return SdrfDataFrame

    def get_sdrf_columns(self):
        """
        This method return the name of the columns of the SDRF.
        :return:
        """
        return self.columns

    @staticmethod
    def parse(sdrf_file: str):
        """
        Read an SDRF into a dataframe
        :param sdrf_file:
        :return:
        """

        df = pd.read_csv(sdrf_file, sep='\t')
        # Convert all columns and values in the dataframe to lowercase
        df = df.astype(str).apply(lambda x: x.str.lower())
        df.columns = map(str.lower, df.columns)

        return SdrfDataFrame(df)

    def validate(self, template: str):
        """
        Validate a corresponding SDRF
        :return:
        """
        errors = []
        if template == HUMAN_TEMPLATE:
            errors = human_schema.validate(self)
        elif template == VERTEBRATES_TEMPLATE:
            errors = vertebrates_chema.validate(self)
        elif template == NON_VERTEBRATES_TEMPLATE:
            errors = nonvertebrates_chema.validate(self)
        elif template == PLANTS_TEMPLATE:
            errors = plants_chema.validate(self)
        elif template == CELL_LINES_TEMPLATE:
            errors = cell_lines_chema.validate(self)
        else:
            errors = default_schema.validate(self)

        for error in errors:
            print(error)
