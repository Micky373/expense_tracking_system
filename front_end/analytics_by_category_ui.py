# Importing useful libraries
import streamlit as st
from datetime import datetime
import requests
import pandas as pd

# Getting the api endpoint for the database
API_URL = "http://localhost:8000"

def analytics_by_category_tab():

    col_1, col_2 = st.columns(2)

    with col_1:

        start_date = st.date_input(label = "Start Date", value = datetime(2024,8,1))

    with col_2:
        
        end_date = st.date_input(label = "End Date", value = datetime(2024,8,5))

    if st.button("Get Analytics"):

        payload = {
            "start_date" : start_date.strftime("%Y-%m-%d"),
            "end_date" : end_date.strftime("%Y-%m-%d")
        }

        response = requests.post(f"{API_URL}/analytics", json = payload)

        result = response.json()

        data = {
            "Category" : list(result.keys()),
            "Totals" : [result[category]['total'] for category in result.keys()],
            "Percentage" : [ round(result[category]['percentage'],2) for category in result.keys()]
        }

        df = pd.DataFrame(data)

        df = df.sort_values(by = "Percentage", ascending = False)

        df = df.set_index("Category")

        st.bar_chart(df['Percentage'])

        st.dataframe(df)

       