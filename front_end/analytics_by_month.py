# Importing useful libraries
import streamlit as st
import requests
import pandas as pd

# Getting the api endpoint for the database
API_URL = "http://localhost:8000"

def analytics_by_month_tab():

    response = requests.get(f"{API_URL}/analytics_monthly/")

    result = response.json()

    data = {
        "Month" : [result[i]['month'] for i in range(len(result))],
        "Total" : [result[i]['total'] for i in range(len(result))]
    }

    df = pd.DataFrame(data)

    df = df.sort_values(by = "Total", ascending = False)

    df = df.set_index("Month")

    st.bar_chart(df['Total'])

    st.dataframe(df)

