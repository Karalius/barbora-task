import pandas as pd
import os, sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(PARENT_DIR)
from app_code.data_dump import DataDump

class DQC:
   """
   Data Quality Checker class for analyzing and reporting data quality.

   This class provides methods to retrieve, analyze, and report data quality
   metrics for database tables.

   Attributes:
      retriever: A DataDump instance for data retrieval.

   Methods:
      describe_table: Get descriptive statistics for a table.
      duplicated_values: Get duplicated values in a table.
      row_count: Get the count of rows in a table.
      unique_values_count: Get the count of unique values in each column of a table.
      missing_values_count: Get the count of missing values in each column of a table.
      row_dtype: Get the data types of columns in a table.
      concat_dqc_tables: Concatenate various data quality metrics into a DataFrame.
      dqc: Generate and save a data quality report for all tables.
   """

   def __init__(self):
      """
      Initialize the DQC instance.

      This method initializes a DataDump instance to retrieve data from
      the database.
      """
      self.retriever = DataDump()
      
   def describe_table(self, table) -> pd.DataFrame:
      """
      Get descriptive statistics for a table.

      Args:
         table (str): The name of the table.

      Returns:
         pd.DataFrame: A DataFrame containing descriptive statistics for the table.
      """
      return round(self.retriever.retrieve_table_data(table).describe(), 2)

   def duplicated_values(self, table) -> pd.DataFrame:
      """
      Get duplicated values in a table.

      Args:
         table (str): The name of the table.

      Returns:
         pd.DataFrame: A DataFrame containing duplicated rows.
      """
      return self.retriever.retrieve_table_data(table)[self.retriever.retrieve_table_data(table).duplicated()]

   def row_count(self, table) -> pd.DataFrame:
      """
      Get the count of rows in a table.

      Args:
            table (str): The name of the table.

      Returns:
            pd.DataFrame: A DataFrame containing the row count.
      """
      return pd.DataFrame(self.retriever.retrieve_table_data(table).count(), columns=['count'])

   def unique_values_count(self, table)-> pd.DataFrame:
      """
      Get the count of unique values in each column of a table.

      Args:
            table (str): The name of the table.

      Returns:
            pd.DataFrame: A DataFrame containing the count of unique values for each column.
      """
      return pd.DataFrame(self.retriever.retrieve_table_data(table).nunique(), columns=['unique_count'])

   def missing_values_count(self, table)-> pd.DataFrame:
      """
      Get the count of missing values in each column of a table.

      Args:
         table (str): The name of the table.

      Returns:
         pd.DataFrame: A DataFrame containing the count of missing values for each column.
      """
      return pd.DataFrame(self.retriever.retrieve_table_data(table).isnull().sum(), columns=['missing_values'])

   def row_dtype(self, table)-> pd.DataFrame:
      """
      Get the data types of columns in a table.

      Args:
         table (str): The name of the table.

      Returns:
         pd.DataFrame: A DataFrame containing the data types of columns.
      """
      return pd.DataFrame(self.retriever.retrieve_table_data(table).dtypes, columns=['dtype'])

   def concat_dqc_tables(self, table) -> pd.DataFrame:
      """
      Concatenate various data quality metrics into a DataFrame.

      Args:
         table (str): The name of the table.

      Returns:
         pd.DataFrame: A DataFrame containing concatenated data quality metrics.
      """
      return pd.concat([
         self.row_count(table),
         self.unique_values_count(table),
         self.missing_values_count(table),
         self.row_dtype(table),
      ], axis=1
      )

   @property
   def dqc(self) -> None:
      """
      Generate and save a data quality report for all tables.

      Generates a data quality report for each table, including duplicated
      values, descriptive statistics, and various data quality metrics.
      The report is saved to a text file.
      """
      with open(f'{PARENT_DIR}/output/data_quality_report.txt', 'a+') as file:
         for table in self.retriever.list_all_db_tables:
            file.write(f'-----------------------------------------------------------------------')
            file.write(f'\nDQC started for {table} table at {pd.Timestamp.now()}\n\n')
            file.write(f'\n{table} duplicated values:\n\n{self.duplicated_values(table).to_string()}')
            file.write(f'\n\n{table} description:\n\n{self.describe_table(table).to_string()}')
            file.write(f'\n\n{table} data quality:\n\n{self.concat_dqc_tables(table).to_string()}')
            file.write(f'\n-----------------------------------------------------------------------')
      print('Succesfully created data quality report.')