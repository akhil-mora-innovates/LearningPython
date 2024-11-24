import streamlit as st
import pandas as pd

# Set Streamlit layout
st.set_page_config(page_title="CRM Dashboard", layout="wide")

# Define CSS for custom KPI styling
st.markdown(
    """
    <style>
    .kpi-widget {
        background-color: #f5f5f5;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
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
