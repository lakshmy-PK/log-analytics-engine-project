import streamlit as st
import plotly.express as px
#import build_pipeline from backend.processing.pipeline
from backend.processing.pipeline import build_pipeline
from backend.anomaly.detector import detect_anomaly

st.title("python based high throughput log analytics monitoring engine")
log_df=build_pipeline("data/sample_log.log")
anomaly_df=detect_anomalies(log_df)
print(anomaly_df)

st.subheadeer("anoalies deteted in logs")
fig=px.line(anomaly_df,x="timestamp",y="value",title="anomaly score over time")
st.plotly_chart(fig)

st.subheader("anomalous log entries")
st.dataframe(anomaly_df)

#filters
threshold=st.sslider("anomaly score threshold",min_value=0.0,max_value=1.0,value=0.5,step=0.01)
filtered_anomaly_df=anomaly_df[anomaly_df["score"]>=threshold]