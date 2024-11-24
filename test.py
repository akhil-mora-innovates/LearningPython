import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(page_title="CRM Dashboard", layout="wide")

# Dashboard title
st.title("🚀 Next-Gen CRM Dashboard")

# First Row: KPIs and Chart
st.markdown("### Overview: Key Performance Indicators (KPIs)")

col1, col2 = st.columns(2)

# Column 1: KPI Widgets
with col1:
    st.metric("Total Leads", "1,245")
    st.metric("Qualified Leads", "845")
    st.metric("Deals Won", "356")
    st.metric("Follow-Up Tasks", "120")
    st.metric("Average Lead Response Time", "2 hrs")
    st.metric("Revenue (This Month)", "$45,670")

# Column 2: Chart
with col2:
    st.markdown("#### Sales Pipeline Overview")
    # Generate a sample chart (you can replace this with real data later)
    data = pd.DataFrame({
        "Stage": ["Prospecting", "Qualified", "Proposal Sent", "Negotiation", "Won"],
        "Count": [150, 120, 90, 50, 30]
    })
    fig, ax = plt.subplots()
    ax.bar(data["Stage"], data["Count"], color="skyblue")
    ax.set_title("Sales Pipeline Stages")
    ax.set_ylabel("Number of Leads")
    ax.set_xlabel("Stages")
    st.pyplot(fig)
