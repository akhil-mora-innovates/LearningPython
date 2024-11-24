import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set Streamlit page configuration
st.set_page_config(page_title="CRM Dashboard", layout="wide")

# Dummy KPI data
kpi_data = [
    {"label": "New Leads", "value": "120", "delta": "+10%"},
    {"label": "Follow-ups", "value": "80", "delta": "-5%"},
    {"label": "Deals Closed", "value": "45", "delta": "+20%"},
    {"label": "Total Revenue", "value": "$50K", "delta": "+15%"},
    {"label": "Pending Tasks", "value": "32", "delta": "-2%"},
    {"label": "Avg Deal Size", "value": "$1.1K", "delta": "+8%"},
]

# Dummy chart data
chart_data = pd.DataFrame({
    "Stage": ["Negotiation", "Proposal Sent", "Prospecting", "Qualified", "Won"],
    "Number of Leads": [30, 50, 150, 120, 20]
})

# Layout for the first row (KPIs and Chart)
col1, col2 = st.columns([2, 3])  # First column for KPIs (40%), second for Chart (60%)

# KPIs Section (First Column)
with col1:
    for row in range(2):  # Divide KPIs into 2 rows
        kpi_cols = st.columns(3)  # 3 KPIs per row
        for idx, col in enumerate(kpi_cols):
            kpi_idx = row * 3 + idx
            if kpi_idx < len(kpi_data):
                kpi = kpi_data[kpi_idx]
                col.metric(label=kpi["label"], value=kpi["value"], delta=kpi["delta"])

# Chart Section (Second Column)
with col2:
    st.subheader("Sales Performance Chart")
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(chart_data["Stage"], chart_data["Number of Leads"], color="steelblue")
    ax.set_title("Sales Stages", fontsize=14)
    ax.set_xlabel("Stage", fontsize=12)
    ax.set_ylabel("Number of Leads", fontsize=12)
    st.pyplot(fig)

# Placeholder for second and third rows
st.markdown("### Second Row (Coming Soon)")
st.markdown("Placeholder for the second row widgets.")
st.markdown("### Third Row (Coming Soon)")
st.markdown("Placeholder for the third row widgets.")
