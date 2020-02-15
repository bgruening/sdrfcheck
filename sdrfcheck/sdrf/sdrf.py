import pandas as pd

from sdrfcheck.sdrf.exceptions import LogicError
from sdrfcheck.sdrf.schemas import human_schema


class SdrfDataFrame(pd.DataFrame):

    @property
    def _constructor(self):
        """
        This method is makes it so our methods return an instance
        :return:
        """
        return SdrfDataFrame

    def get_sdrf_cloumns(self):
        """
        This method return the name of the columns of the SDRF.
        :return:
        """
        return self.columns

    @staticmethod
    def parse(sdrf_file : str):
        df = pd.read_csv(sdrf_file, sep='\t')
        return SdrfDataFrame(df)

    def validate(self):
        """
        Validate a corresponding SDRF
        :return:
        """
        errors = human_schema.validate(self)
        errors = LogicError.process_errors(errors)
        for error in errors:
            print(error)









