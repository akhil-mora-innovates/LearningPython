import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set Streamlit page configuration
st.set_page_config(page_title="CRM Dashboard", layout="wide")

# Custom CSS for modern UI design
st.markdown("""
    <style>
        body {
            background-color: #f8f9fc;
        }
        .container {
            padding: 20px;
        }
        .kpi-container {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 15px;
        }
        .kpi-card {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 15px;
            text-align: center;
        }
        .kpi-title {
            font-size: 14px;
            color: #6c757d;
            margin-bottom: 5px;
        }
        .kpi-value {
            font-size: 24px;
            font-weight: bold;
            color: #212529;
        }
        .kpi-delta {
            font-size: 14px;
            margin-top: 5px;
            color: #28a745; /* Green for positive */
        }
        .kpi-delta.negative {
            color: #dc3545; /* Red for negative */
        }
        .chart-container {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# KPI Data
kpi_data = [
    {"label": "New Leads", "value": "120", "delta": "+10%", "positive": True},
    {"label": "Follow-ups", "value": "80", "delta": "-5%", "positive": False},
    {"label": "Deals Closed", "value": "45", "delta": "+20%", "positive": True},
    {"label": "Total Revenue", "value": "$50K", "delta": "+15%", "positive": True},
    {"label": "Pending Tasks", "value": "32", "delta": "-2%", "positive": False},
    {"label": "Avg Deal Size", "value": "$1.1K", "delta": "+8%", "positive": True},
]

# Sales Performance Data for Chart
chart_data = pd.DataFrame({
    "Stage": ["Negotiation", "Proposal Sent", "Prospecting", "Qualified", "Won"],
    "Number of Leads": [30, 50, 150, 120, 20]
})

# Layout for the first row
col1, col2 = st.columns([2, 3], gap="medium")  # KPIs take 40%, Chart takes 60%

# KPIs Section
with col1:
    st.markdown('<div class="kpi-container">', unsafe_allow_html=True)
    for kpi in kpi_data:
        delta_class = "kpi-delta" if kpi["positive"] else "kpi-delta negative"
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-title">{kpi['label']}</div>
                <div class="kpi-value">{kpi['value']}</div>
                <div class="{delta_class}">{kpi['delta']}</div>
            </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Chart Section
with col2:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<h4 style="margin-top: 0; color: #212529;">Sales Performance</h4>', unsafe_allow_html=True)

    # Bar chart
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(chart_data["Stage"], chart_data["Number of Leads"], color="#4e73df")
    ax.set_title("Sales Stages", fontsize=14, color="#212529")
    ax.set_xlabel("Stage", fontsize=12)
    ax.set_ylabel("Number of Leads", fontsize=12)
    st.pyplot(fig)
    st.markdown('</div>', unsafe_allow_html=True)
