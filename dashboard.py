import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Log Dashboard", layout="wide")
st.title("📊 Log Analytics Dashboard")

log_file = "backend/data/realtime_logs.csv"

if not os.path.exists(log_file):
    st.error("Log file not found. First run log_generator.py")
    st.stop()

df = pd.read_csv(log_file)
df["timestamp"] = pd.to_datetime(df["timestamp"])

error_df = df[df["level"] == "ERROR"]
info_df = df[df["level"] == "INFO"]
warn_df = df[df["level"] == "WARN"]

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("ERROR Logs")
    st.bar_chart(error_df["level"].value_counts())

with col2:
    st.subheader("INFO Logs")
    st.bar_chart(info_df["level"].value_counts())

with col3:
    st.subheader("WARN Logs")
    st.bar_chart(warn_df["level"].value_counts())