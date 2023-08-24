import pytest
import pandas as pd
import os, sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(PARENT_DIR)

from app_code.data_dump import DataDump
from app_code.data_quality import DQC
from unittest.mock import Mock

class TestDQC:
    """
    Test class for the DQC (Data Quality Checker) methods.

    This class contains test methods for various methods of the DQC class,
    which analyze and report data quality metrics.

    Methods:
        setup_method: Setup method to initialize the DQC instance and its mock retriever.
        test_describe_table: Test method for the describe_table method.
        test_duplicated_values: Test method for the duplicated_values method.
        test_row_count: Test method for the row_count method.
        test_unique_values_count: Test method for the unique_values_count method.
        test_missing_values_count: Test method for the missing_values_count method.
        test_row_dtype: Test method for the row_dtype method.
    """

    def setup_method(self):
        """
        Setup method to initialize the DQC instance and its mock retriever.

        This method is automatically run before each test method and initializes
        a DQC instance with a mock retriever.
        """
        self.dqc = DQC()
        self.dqc.retriever = Mock()
        
    def test_describe_table(self):
        """
        Test the describe_table method.

        This test sets up a mock DataFrame and checks whether the describe_table
        method returns a pandas DataFrame.
        """
        self.dqc.retriever.retrieve_table_data.return_value = pd.DataFrame({
            'column1': [1, 2, 3, 4, 5],
            'column2': [10, 20, 30, 40, 50]
        })
        result = self.dqc.describe_table("dummy_table")
        assert isinstance(result, pd.DataFrame)
        
    def test_duplicated_values(self):
        """
        Test the duplicated_values method.

        This test sets up a mock DataFrame and checks whether the duplicated_values
        method returns a pandas DataFrame.
        """
        self.dqc.retriever.retrieve_table_data.return_value = pd.DataFrame({
            'column1': [1, 2, 2, 3, 4],
            'column2': [10, 20, 20, 30, None],
            'column3': ['A', 'B', 'A', 'C', 'D']
        })
        result = self.dqc.duplicated_values("dummy_table")
        assert isinstance(result, pd.DataFrame)
        
    def test_row_count(self):
        """
        Test the row_count method.

        This test sets up a mock DataFrame and checks whether the row_count
        method returns a pandas DataFrame.
        """
        self.dqc.retriever.retrieve_table_data.return_value = pd.DataFrame({
            'column1': [1, 2, 3, 4, 5],
            'column2': [10, 20, 30, 40, 50]
        })
        result = self.dqc.row_count("dummy_table")
        assert isinstance(result, pd.DataFrame)
        
    def test_unique_values_count(self):
        """
        Test the unique_values_count method.

        This test sets up a mock DataFrame and checks whether the unique_values_count
        method returns a pandas DataFrame.
        """
        self.dqc.retriever.retrieve_table_data.return_value = pd.DataFrame({
            'column1': [1, 2, 2, 3, 4],
            'column2': [10, 20, 20, 30, None],
            'column3': ['A', 'B', 'A', 'C', 'D']
        })
        result = self.dqc.unique_values_count("dummy_table")
        assert isinstance(result, pd.DataFrame)
        
    def test_missing_values_count(self):
        """
        Test the missing_values_count method.

        This test sets up a mock DataFrame and checks whether the missing_values_count
        method returns a pandas DataFrame.
        """
        self.dqc.retriever.retrieve_table_data.return_value = pd.DataFrame({
            'column1': [1, 2, 3, 4, 5],
            'column2': [None, 20, 30, 40, None],
            'column3': ['A', None, 'C', None, 'D']
        })
        result = self.dqc.missing_values_count("dummy_table")
        assert isinstance(result, pd.DataFrame)
        
    def test_row_dtype(self):
        """
        Test the row_dtype method.

        This test sets up a mock DataFrame and checks whether the row_dtype
        method returns a pandas DataFrame.
        """
        self.dqc.retriever.retrieve_table_data.return_value = pd.DataFrame({
            'column1': [1, 2, 3, 4, 5],
            'column2': [10, 20, 30, 40, 50],
            'column3': ['A', 'B', 'C', 'D', 'E']
        })
        result = self.dqc.row_dtype("dummy_table")
        assert isinstance(result, pd.DataFrame)
        
if __name__ == '__main__':
    pytest.main()