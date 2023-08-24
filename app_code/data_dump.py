import pandas as pd
import os, sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(PARENT_DIR)
from app_code.database import Database

class DataDump:
   """
   Simple way to dump all database tables to an Excel file.

   This class provides methods to connect to a database, retrieve data from its
   tables, and dump each table's data into separate Excel sheets within a single
   Excel file.

   Attributes:
      connection: The database connection established using the Database class.

   Methods:
      list_all_db_tables: List all tables present in the connected database.
      retrieve_table_data: Query all rows and columns from a selected table.
      dump: Dump each database table's data as separate Excel sheets in a file.
   """
   
   def __init__(self):
      """
      Initialize the DataDump instance.

      This method establishes a connection to the database using the Database
      class and stores it as the 'connection' attribute.
      """
      self.connection = Database().connection

   @property
   def list_all_db_tables(self) -> list:
      """
      List all tables present in the database.

      Returns:
         list: A list containing the names of all tables in the database.
      """
      tables = list(pd.read_sql_query('SELECT name FROM sys.tables', self.connection).name)
      return tables

   def retrieve_table_data(self, table) -> pd.DataFrame:
      """
      Retrieve all rows and columns from the selected database table.

      Args:
         table (str): The name of the table to retrieve data from.

      Returns:
         pd.DataFrame: A pandas DataFrame containing the retrieved data.
      """
      return pd.read_sql_query(f'SELECT * FROM {table}', self.connection)

   @property
   def dump(self) -> None:
      """
      Dump database tables' data to an Excel file.

      Dumps each database table's data as a separate Excel sheet within a
      single Excel file and saves it in the 'output' directory.
      """
      with pd.ExcelWriter(f'{PARENT_DIR}/output/data_dump.xlsx') as writer:
         for table in self.list_all_db_tables:
            self.retrieve_table_data(table).to_excel(writer, sheet_name=f'{table}', header=True, index=False)
      print('Succesfully transferred data to excel file.')