import streamlit as st
import pandas as pd
import altair as alt

# Set up the layout
st.set_page_config(layout="wide")

# Dummy KPI Data
kpi_data = [
    {"label": "New Leads", "value": "120", "change": "+10%"},
    {"label": "Follow-ups", "value": "80", "change": "-5%"},
    {"label": "Deals Closed", "value": "45", "change": "+20%"},
    {"label": "Total Revenue", "value": "$50K", "change": "+15%"},
    {"label": "Pending Tasks", "value": "32", "change": "-2%"},
    {"label": "Avg Deal Size", "value": "$1.1K", "change": "+8%"},
]

# Dummy Sales Data
data = pd.DataFrame({
    "Stage": ["Negotiation", "Proposal Sent", "Prospecting", "Qualified", "Won"],
    "Number of Leads": [50, 80, 150, 120, 30],
})

# Create Layout: First Row with KPIs and Chart
row1_col1, row1_col2 = st.columns([2, 3])

# KPIs Section
with row1_col1:
    kpi_col1, kpi_col2, kpi_col3 = st.columns(3)
    for idx, kpi in enumerate(kpi_data):
        with [kpi_col1, kpi_col2, kpi_col3][idx % 3]:
            st.metric(label=kpi["label"], value=kpi["value"], delta=kpi["change"])

# Chart Section
with row1_col2:
    st.markdown("### Sales Performance Chart")
    chart = (
        alt.Chart(data)
        .mark_bar()
        .encode(x="Stage", y="Number of Leads", tooltip=["Stage", "Number of Leads"])
        .properties(height=300)
    )
    st.altair_chart(chart, use_container_width=True)

st.divider()

# Space for future rows
st.write("Second and third rows coming soon...")
