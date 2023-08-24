import os
import sys
import pytest

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(PARENT_DIR)

from app_code.database import Database
from sqlalchemy.engine import Engine

@pytest.fixture(autouse=True)
def mock_os_environ(mocker):
    """
    Mocks the os.environ dictionary with database credentials.

    This fixture is automatically used by all tests to mock the os.environ dictionary
    with dummy database credentials for testing purposes.

    Args:
        mocker: The pytest mocker object used for patching.
    """
    mocker.patch.dict(os.environ, {
        'DB_USER': 'test_user',
        'DB_PASSWORD': 'test_password',
        'DB_HOST': 'test_host',
        'DB_PORT': '1433',
        'DB_NAME': 'test_db'
    })

def test_database_connection_success():
    """
    Test the successful establishment of a database connection.

    This test checks whether a database connection is successfully established
    by creating an instance of the Database class and asserting the connection
    attribute's existence and type.
    """
    db = Database()
    
    assert db.connection is not None
    assert isinstance(db.connection, Engine)