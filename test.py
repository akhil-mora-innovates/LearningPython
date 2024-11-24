import streamlit as st
import pandas as pd
import altair as alt

# Set Streamlit layout
st.set_page_config(page_title="CRM Dashboard", layout="wide")

# Define CSS for styling
st.markdown(
    """
    <style>
    /* Overall App Background Color */
    body {
        background-color: #f0f2f6; /* Light grayish blue */
    }

    /* Custom Style for KPI Widgets */
    .kpi-widget {
        background-color: white; /* Widget Background */
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Subtle shadow */
        margin: 10px;
    }
    .kpi-title {
        font-size: 20px;
        color: #333333;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .kpi-value {
        font-size: 30px;
        color: #007BFF; /* Blue text */
        font-weight: bold;
    }
    .kpi-delta {
        font-size: 16px;
        color: #28a745; /* Green for positive deltas */
    }
    .kpi-negative {
        color: #dc3545; /* Red for negative deltas */
    }

    /* Chart Container Styling */
    .chart-container {
        background-color: white; /* Chart Background */
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Subtle shadow */
        margin: 10px;
    }
    .chart-title {
        font-size: 24px;
        font-weight: bold;
        color: #333333;
        text-align: center;
        margin-bottom: 20px;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #ffffff; /* White Sidebar */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

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

# Styled container for chart and title
st.markdown('<div class="chart-container">', unsafe_allow_html=True)
st.markdown('<div class="chart-title">Sales Performance Chart</div>', unsafe_allow_html=True)
st.altair_chart(chart, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)
