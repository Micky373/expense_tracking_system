# Importing useful libraries
import mysql.connector # A library to connect with MySql
from contextlib import contextmanager # Used for managing resource
import os # A library for performing operating system related tasks
from dotenv import load_dotenv # For getting environment variables
from pathlib import Path # For path related tasks
from logging_setup import setup_logger

# Construct the path to the .env file in the parent directory
dotenv_path = Path('../.env')

# Initializing the password and user
load_dotenv()
user = os.environ.get("DATABASE_USER")
password = os.environ.get("DATABASE_PASSWORD")

# Load environment variables from .env file
load_dotenv()

# Setting up and getting the logger
logger = setup_logger('db_helper')

# A function to create a connection with the database
@contextmanager
def get_db_cursor( commit = False, user = user, password = password):
    logger.info("Connecting to the database...")
    connection = mysql.connector.connect(
        host = "localhost" ,
        user = user ,
        password = password ,
        database = "expense_manager"
    )

    cursor = connection.cursor(dictionary=True)
    yield cursor

    if commit:
        connection.commit()
    cursor.close()
    connection.close()
    logger.info("Closing the connection...")


# A function to retreive all the records
def fetch_all_records():
    logger.info("Fetching all the records")
    query = "SELECT * from expenses"

    with get_db_cursor() as cursor:
        cursor.execute(query)
        expenses = cursor.fetchall()

        logger.info("Successfully fetched all the records!!!")        
        return expenses

# A function to fetch certain records for a certain date
def fetch_expenses_for_date(expense_date):
    logger.info(f"Fetching the expense on date {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        logger.info(f"Successfully fetched the expense on date {expense_date}!!!") 
        return expenses

# A function to insert expenses givend date, amount, category and notes
def insert_expense(expense_date, amount, category, notes):
    logger.info(f"Inserting this expense date : {expense_date}, amount : {amount}, category : {category}, notes : {notes} ")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
            (expense_date, amount, category, notes)
        )
    logger.info(f"Successfully inserted this expense date : {expense_date}, amount : {amount}, category : {category}, notes : {notes} ")

# A function to delete expense for a certain date
def delete_expenses_for_date(expense_date):
    logger.info(f"Deleting the record at the date : {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))
    logger.info(f"Successfully deleted the record at the date : {expense_date}!!!")


# A function to get expense summary in a given date range
def fetch_expense_summary( start_date , end_date ):

    logger.info(f"Fetching the expenses from {start_date} to {end_date}")

    with get_db_cursor() as cursor:

        cursor.execute(
            ''' SELECT category, SUM(amount) AS total
                FROM expenses WHERE expense_date
                BETWEEN %s AND %s
                GROUP BY category;
            ''',
            ( start_date, end_date)
        )

        data = cursor.fetchall()

        logger.info(f"Successfully finished fetching the expenses from {start_date} to {end_date}")

        return data
    

# A function to get expense summary for the monthly
def get_monthly_analysis( ):

    logger.info(f"Fetching the monthly analysis")

    with get_db_cursor() as cursor:

        cursor.execute(
            ''' 
            SELECT MONTHNAME(expense_date) AS month, SUM(amount) AS total 
            FROM expenses GROUP BY month 
            '''
        )

        data = cursor.fetchall()

        logger.info(f"Successfully finished fetched the monthly analysis")
        
        return data
