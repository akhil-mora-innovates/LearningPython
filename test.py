import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# CSS styles for the app
st.markdown("""
    <style>
        .main-container {
            background-color: #f5f5f5;
            padding: 20px;
        }
        .kpi-container {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-right: 20px;
        }
        .kpi-card {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            padding: 15px;
            flex: 1 1 calc(33% - 20px);
            min-width: 150px;
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
            color: #343a40;
            margin-bottom: 5px;
        }
        .kpi-change {
            font-size: 14px;
            color: #28a745; /* Green */
        }
        .kpi-change.negative {
            color: #dc3545; /* Red */
        }
        .chart-container {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            padding: 15px;
            width: 60%;
        }
    </style>
""", unsafe_allow_html=True)

# Layout for the first row
st.markdown('<div class="main-container">', unsafe_allow_html=True)
col1, col2 = st.columns([2, 3], gap="medium")

# Column 1: KPIs
with col1:
    st.markdown('<div class="kpi-container">', unsafe_allow_html=True)
    kpis = [
        {"title": "New Leads", "value": "120", "change": "+10%", "positive": True},
        {"title": "Follow-ups", "value": "80", "change": "-5%", "positive": False},
        {"title": "Deals Closed", "value": "45", "change": "+20%", "positive": True},
        {"title": "Total Revenue", "value": "$50K", "change": "+15%", "positive": True},
        {"title": "Pending Tasks", "value": "32", "change": "-2%", "positive": False},
        {"title": "Avg Deal Size", "value": "$1.1K", "change": "+8%", "positive": True},
    ]

    for kpi in kpis:
        change_class = "kpi-change negative" if not kpi["positive"] else "kpi-change"
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-title">{kpi["title"]}</div>
                <div class="kpi-value">{kpi["value"]}</div>
                <div class="{change_class}">{kpi["change"]}</div>
            </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Column 2: Chart
with col2:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<h4 style="margin-top: 0;">Sales Performance Chart</h4>', unsafe_allow_html=True)

    # Dummy data for the chart
    data = pd.DataFrame({
        "Stage": ["Negotiation", "Proposal Sent", "Prospecting", "Qualified", "Won"],
        "Number of Leads": [30, 50, 100, 80, 20]
    })

    # Plotting the chart
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.bar(data["Stage"], data["Number of Leads"], color="steelblue")
    ax.set_title("Sales Stages")
    ax.set_xlabel("Stages")
    ax.set_ylabel("Number of Leads")
    st.pyplot(fig)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
