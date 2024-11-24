import streamlit as st
import pandas as pd

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

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #ffffff; /* White Sidebar */
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# Create layout with 3 rows and 2 columns
row1_col1, row1_col2 = st.columns(2)

# Row 1, Column 1: KPIs in a 2x3 grid
with row1_col1:
    st.markdown("### Key Performance Indicators")

    # Helper function to render custom-styled KPIs
    def kpi_widget(title, value, delta, delta_positive=True):
        delta_class = "kpi-delta" if delta_positive else "kpi-delta kpi-negative"
        st.markdown(
            f"""
            <div class="kpi-widget">
                <div class="kpi-title">{title}</div>
                <div class="kpi-value">{value}</div>
                <div class="{delta_class}">{delta}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # First Row of KPIs
    col1, col2, col3 = st.columns(3)
    with col1:
        kpi_widget("New Leads", "120", "+10%")
    with col2:
        kpi_widget("Follow-ups", "80", "-5%", delta_positive=False)
    with col3:
        kpi_widget("Deals Closed", "45", "+20%")

    # Second Row of KPIs
    col4, col5, col6 = st.columns(3)
    with col4:
        kpi_widget("Total Revenue", "$50K", "+15%")
    with col5:
        kpi_widget("Pending Tasks", "32", "-2%", delta_positive=False)
    with col6:
        kpi_widget("Avg Deal Size", "$1.1K", "+8%")

# Row 1, Column 2: Chart with Styling
with row1_col2:
    st.markdown("### Sales Performance Chart")

    # Define data with ordered stages
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

    # Add chart container styling
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.bar_chart(data.set_index("Stage"))
    st.markdown('</div>', unsafe_allow_html=True)

# Placeholder for additional rows
st.write("Row 2 and Row 3 content goes here.")
