# app/main.py

import streamlit as st
from utils import load_data, plot_metric_boxplot, summary_table


st.set_page_config(page_title="Cross-Country Solar Comparison", layout="wide")

st.title("☀️ Cross-Country Solar Data Dashboard")

df = load_data()

# Show Summary Table
st.subheader("📊 Summary Statistics")
st.dataframe(summary_table(df))

# Boxplots
st.subheader("📦 Metric Comparison by Country")
metric = st.selectbox("Choose a metric", ["GHI", "DNI", "DHI"])
fig = plot_metric_boxplot(df, metric)
st.plotly_chart(fig, use_container_width=True)

# Average GHI Bar Chart
st.subheader("🏆 Country Ranking by Average GHI")
avg_ghi = df.groupby("Country")["GHI"].mean().sort_values(ascending=False)
st.bar_chart(avg_ghi)
