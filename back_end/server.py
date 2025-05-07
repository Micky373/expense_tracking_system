# Importing useful libraries
from fastapi import FastAPI, HTTPException # For backend related tasks
from datetime import date # For date and time related tasks
from db_helper import * # Importing all the functions from our db_helper module
from typing import List # For list related tasks
from pydantic import BaseModel # For formating related tasks

# Initializing a base model for the object we send and recieve while get and post method
class Expense(BaseModel):

    amount : float
    category : str
    notes : str

# Initializing the base model for date range
class DateRange(BaseModel):

    start_date : date
    end_date :  date

# Initializing the app
app = FastAPI()

# Creating a get method to retrieve an info on that date
@app.get("/expenses/{expense_date}", response_model = List[Expense])
def get_expense( expense_date : date ):

    data = fetch_expenses_for_date(expense_date)

    return data

# Creating a post method to add an expense on a given date
@app.post("/expenses/{expense_date}")
def add_expense( expense_date : date, expenses : List[Expense]  ):

    delete_expenses_for_date(expense_date)

    for expense in expenses:

        insert_expense(expense_date, expense.amount, expense.category, expense.notes )

    return {"message": "Expenses updated successfully"}

# Creating a post method for getting summarized analysis
@app.post("/analytics/")
def analytics(date_range : DateRange):

    data = fetch_expense_summary(date_range.start_date, date_range.end_date)

    if data:

        total_expense = sum([row['total'] for row in data])

        break_down = {}

        for row in data:

            percentage = (row['total'] / total_expense) * 100 if total_expense != 0 else 0

            break_down[row['category']] = {
                "total" : row['total'],
                "percentage" : percentage
            }

    else:

        raise HTTPException(status_code = 500, detail = "Failed to retreive data from our database") 
    
    return break_down

# Creating a get method for getting summarized analyis
@app.get("/analytics_monthly/")
def analytics_monthly():

    data = get_monthly_analysis()

    return data
        
