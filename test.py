import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# CSS styles to mimic the template UI
st.markdown("""
    <style>
        body {
            background-color: #f9fafc;
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
            font-size: 16px;
            color: #6b7280;
            margin-bottom: 8px;
        }
        .kpi-value {
            font-size: 24px;
            font-weight: bold;
            color: #111827;
            margin-bottom: 5px;
        }
        .kpi-change {
            font-size: 14px;
            font-weight: bold;
        }
        .kpi-change.positive {
            color: #22c55e;
        }
        .kpi-change.negative {
            color: #ef4444;
        }
        .chart-container {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Layout for the first row (KPIs and Chart)
st.markdown('<div class="container">', unsafe_allow_html=True)
col1, col2 = st.columns([3, 4], gap="medium")

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
        change_class = "kpi-change positive" if kpi["positive"] else "kpi-change negative"
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
    st.markdown('<h4 style="margin-top: 0; color: #111827;">Sales Performance</h4>', unsafe_allow_html=True)

    # Dummy data for the chart
    data = pd.DataFrame({
        "Stage": ["Negotiation", "Proposal Sent", "Prospecting", "Qualified", "Won"],
        "Number of Leads": [30, 50, 100, 80, 20]
    })

    # Plotting the chart
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.bar(data["Stage"], data["Number of Leads"], color="#6366f1")
    ax.set_title("Sales Stages", fontsize=14, color="#111827")
    ax.set_xlabel("Stages", fontsize=12)
    ax.set_ylabel("Number of Leads", fontsize=12)
    st.pyplot(fig)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
