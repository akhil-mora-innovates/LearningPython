import streamlit as st
import pandas as pd
import altair as alt

# Set Streamlit page configuration
st.set_page_config(page_title="CRM Dashboard", layout="wide")

# Layout for first row (2 columns)
col1, col2 = st.columns([2, 1])  # Column 1 takes 2/3 of the space, Column 2 takes 1/3

# First column of the first row: 6 KPIs (2 rows, 3 columns)
with col1:
    # Create 2x3 grid for KPIs
    row1_col1, row1_col2, row1_col3 = st.columns(3)
    with row1_col1:
        st.subheader("New Leads")
        st.metric("120", "+10%")
    
    with row1_col2:
        st.subheader("Follow-ups")
        st.metric("80", "-5%")
    
    with row1_col3:
        st.subheader("Deals Closed")
        st.metric("45", "+20%")

    # Second row of KPIs
    row2_col1, row2_col2, row2_col3 = st.columns(3)
    with row2_col1:
        st.subheader("Total Revenue")
        st.metric("$50K", "+15%")
    
    with row2_col2:
        st.subheader("Pending Tasks")
        st.metric("32", "-2%")
    
    with row2_col3:
        st.subheader("Avg Deal Size")
        st.metric("$1.1K", "+8%")

# Second column of the first row: Sales Performance Chart
with col2:
    # Data for the chart
    data = pd.DataFrame({
        "Stage": ["Prospecting", "Qualified", "Proposal Sent", "Negotiation", "Won"],
        "Count": [150, 120, 90, 50, 30]
    })

    # Ensure stages are ordered as defined in the dataframe
    data["Stage"] = pd.Categorical(
        data["Stage"],
        categories=["Prospecting", "Qualified", "Proposal Sent", "Negotiation", "Won"],
        ordered=True
    )

    # Create Altair Chart
    chart = alt.Chart(data).mark_bar(cornerRadiusTopLeft=5, cornerRadiusTopRight=5).encode(
        x=alt.X("Stage", sort="x", title="Sales Stages"),
        y=alt.Y("Count", title="Number of Leads"),
        tooltip=["Stage", "Count"]
    ).properties(
        width=500,
        height=400
    ).configure_axis(
        labelFontSize=12,
        titleFontSize=14
    )

    # Display Chart with Title
    st.subheader("Sales Performance Chart")
    st.altair_chart(chart, use_container_width=True)

# Placeholder for second row
st.markdown('### Second Row')
st.markdown('Placeholder for second row widgets.')

# Placeholder for third row
st.markdown('### Third Row')
st.markdown('Placeholder for third row widgets.')
