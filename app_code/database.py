from sqlalchemy.engine import URL
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

class Database:
   """
   Connects to SQL Server.

   This class provides methods to establish a connection to a SQL Server
   database using the provided credentials and connection URL.

   Attributes:
      __connection: The database connection created using SQLAlchemy.

   Methods:
      connection: Get the established database connection.
   """
   
   def __init__(self):
      """
      Initialize the Database instance.

      This method retrieves database credentials from environment variables,
      creates a connection URL, and establishes a database connection.
      """
      try:
         load_dotenv()
         
         connect_url = URL.create(
               'mssql+pyodbc',
               username=os.environ.get('DB_USER'),
               password=os.environ.get('DB_PASSWORD'),
               host=os.environ.get('DB_HOST'),
               port=os.environ.get('DB_PORT'),
               database=os.environ.get('DB_NAME'),
               query=dict(driver='ODBC Driver 17 for SQL Server')
         )
         self.__connection = create_engine(connect_url)
      except Exception as error:
         print(f"Error: Connection not established - {error}")
         self.__connection = None
   
   @property
   def connection(self) -> None:
      """
      Get the established database connection.

      Returns:
         sqlalchemy.engine.base.Connection: The established database connection.
      """
      return self.__connection