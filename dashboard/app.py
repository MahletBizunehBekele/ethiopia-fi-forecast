import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Ethiopia Financial Inclusion Dashboard")

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(BASE_DIR / "data" / "raw" / "ethiopia_fi_unified_data.csv")
st.metric("Records", len(df))

st.metric(
    "Observations",
    len(df[df.record_type=="observation"])
)

st.metric(
    "Events",
    len(df[df.record_type=="event"])
)

counts = df.record_type.value_counts()

fig,ax = plt.subplots()

counts.plot.bar(ax=ax)

st.pyplot(fig)