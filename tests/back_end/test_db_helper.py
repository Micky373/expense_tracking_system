# Importing useful libraries

# Two libraries to work with operating system related tasks
import sys
import os


# Getting the path to our parent folder
current_dir = os.path.dirname(os.path.abspath(__file__))

parent_dir = os.path.dirname(os.path.dirname(current_dir))

# Appending our parent directory to the system path list
sys.path.append(parent_dir)

# Getting our db_helper function for test
from back_end import db_helper


# Creating a test if our function fetches correctly
def test_fetch_expenses_for_date():

    expenses = db_helper.fetch_expenses_for_date("2024-08-01")

    assert len(expenses) == 4
    assert expenses[0]['id'] == 63
    assert expenses[1]['amount'] == 300
    assert expenses[2]['category'] == "Rent"

# Creating a test if we give invalid date range
def test_fetch_expense_for_invalid_date():

    expenses = db_helper.fetch_expenses_for_date("9999-12-30")

    assert len(expenses) == 0

# Creating a test if we give invalid date range
def test_fetch_expense_summary_invalid_date_range():

    expenses = db_helper.fetch_expense_summary( "9999-12-30" , "9979-12-30" )

    assert len(expenses) == 0