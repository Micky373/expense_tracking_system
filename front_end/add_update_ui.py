# Importing useful libraries
import streamlit as st # For front end 
from datetime import datetime
import requests

# Getting the api endpoint for the database
API_URL = "http://localhost:8000"

# A function for displaying the add and update functionality
def add_update_tab():
    
    # Getting the date for the adding or updating 
    selected_date = st.date_input("Enter Date", datetime(2024,8,1), label_visibility = "collapsed")

    # Sending a get request for our FastAPI back end
    response = requests.get(f"{API_URL}/expenses/{selected_date}")

    # Returngin the response if the status is successful
    if response.status_code == 200 :

        existing_expense = response.json()

    else:

        st.error("Failed to retreive the data!!!")

        existing_expense = []

    # Creating the categories list
    categories = [
        "Rent",
        "Food",
        "Shopping",
        "Entertainment",
        "Other"
    ]

    # Creating a form for displaying the data we fetch from the back end
    with st.form(key = "expense_form"):

        col_1, col_2, col_3 = st.columns(3)

        with col_1:

            st.subheader("Amount")

        with col_2:

            st.subheader("Category")

        with col_3:

            st.subheader("Notes")

        expenses = []

        # Displaying all the categories
        for i in range(5):
            
            # Checking if we have a data for that date and displaying
            if i < len(existing_expense):

                if len(existing_expense) != 0:
                    amount = existing_expense[i]['amount']

                    category = existing_expense[i]['category']

                    category_index = categories.index(category)

                    note = existing_expense[i]['notes']

            else:

                amount, category_index, note = 0.0, 0, " "

            col_1, col_2, col_3 = st.columns(3)

            with col_1:
                
                expense_amount = st.number_input(label = "Amount", min_value = 0.0, step = 1.0, value = amount, key = f"amount_{i}", label_visibility = "collapsed")
            
            with col_2:
                
                expense_category = st.selectbox(label = "Category",options = categories, 
                                                index = category_index if len(existing_expense) != 0 else i, 
                                                key = f"category_{i}", label_visibility = "collapsed")
            
            with col_3:
                
                expense_note = st.text_area(label = "Notes", value = note, key = f"notes_{i}", label_visibility = "collapsed")

            # Appending the results so that we can do the updates later
            expenses.append({
                'amount' : expense_amount,
                'category' : expense_category,
                'notes' : expense_note
            })
        
        # Creating a submit button for updating or adding the expense
        submit_button = st.form_submit_button("Submit")

        if submit_button:

            # Updating only the expenses that a user has spent more than 0
            filtered_expenses = [expense for expense in expenses if expense['amount'] > 0]

            # Creating a post request for our back end to update the expense at that given date
            response = requests.post(f"{API_URL}/expenses/{selected_date}", json = filtered_expenses)

            # Displaying success if our post request is returning status code of 200
            if response.status_code == 200:

                st.success("Expense Updated Successfully!!!")

            else: st.error("Failed to update expenses")