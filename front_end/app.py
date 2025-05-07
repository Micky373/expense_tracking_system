# Importing useful libraries
import streamlit as st
from add_update_ui import add_update_tab
from analytics_by_category_ui import analytics_by_category_tab  
from analytics_by_month import analytics_by_month_tab

# Creating a title for our webpage
st.title("Expense Tracking System")

# Creating two tabs for displaying the analytics and updating the records
tab_1 , tab_2, tab_3 = st.tabs(["Add/Update" , "Analytics By Category", "Analytics By Month"])

# A tab for updating records
with tab_1:

    add_update_tab()

# A tab for analytics purpose
with tab_2:

    analytics_by_category_tab()

# A tab for analytics by month
with tab_3:

    analytics_by_month_tab()

