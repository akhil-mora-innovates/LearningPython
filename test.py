import streamlit as st
import pandas as pd

# Set Streamlit layout
st.set_page_config(page_title="CRM Dashboard", layout="wide")

# Create layout with 3 rows and 2 columns
row1_col1, row1_col2 = st.columns(2)

# Row 1, Column 1: KPIs in a 2x3 grid
with row1_col1:
    st.markdown("### Key Performance Indicators")
    col1, col2, col3 = st.columns(3)  # First row of KPIs
    col4, col5, col6 = st.columns(3)  # Second row of KPIs

    # First Row of KPIs
    col1.metric("New Leads", "120", "+10%")
    col2.metric("Follow-ups", "80", "-5%")
    col3.metric("Deals Closed", "45", "+20%")

    # Second Row of KPIs
    col4.metric("Total Revenue", "$50K", "+15%")
    col5.metric("Pending Tasks", "32", "-2%")
    col6.metric("Avg Deal Size", "$1.1K", "+8%")

# Row 1, Column 2: Chart
with row1_col2:
    st.markdown("### Sales Performance Chart")
    data = pd.DataFrame({
        "Stage": ["Prospecting", "Qualified", "Proposal Sent", "Negotiation", "Won"],
        "Count": [150, 120, 90, 50, 30]
    })
    st.bar_chart(data.set_index("Stage"))

# Example placeholders for Row 2 and Row 3 (to be filled later)
st.write("Row 2 and Row 3 content goes here.")
