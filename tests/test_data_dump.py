import pytest
import os, sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(PARENT_DIR)

from app_code.data_dump import DataDump
import pandas as pd

@pytest.fixture
def data_dump_instance():
    """
    Fixture to create a DataDump instance.

    Returns:
        DataDump: An instance of the DataDump class.
    """
    return DataDump()

def test_list_all_db_tables(data_dump_instance):
    """
    Test the list_all_db_tables method.

    This test checks whether the list_all_db_tables method returns the expected list of tables.

    Args:
        data_dump_instance (DataDump): An instance of the DataDump class.
    """
    expected_tables = ['categories', 'brands', 'products', 'customers', 'stores', 'staffs', 'orders', 'order_items', 'stocks']
    actual_tables = data_dump_instance.list_all_db_tables

    assert actual_tables == expected_tables


def test_retrieve_table_data(data_dump_instance):
    """
    Test the retrieve_table_data method.

    This test checks whether the retrieve_table_data method returns the expected data for a specific table.

    Args:
        data_dump_instance (DataDump): An instance of the DataDump class.
    """
    test_table_name = "categories"
    expected_data = pd.DataFrame([(1, "Children Bicycles"), (2, "Comfort Bicycles"), (3, "Cruisers Bicycles"), (4, "Cyclocross Bicycles"),
                                  (5, "Electric Bikes"), (6, "Mountain Bikes"),(7, "Road Bikes")], columns=["category_id", "category_name"])
    
    actual_data = data_dump_instance.retrieve_table_data(test_table_name)
    pd.testing.assert_frame_equal(actual_data, expected_data)
