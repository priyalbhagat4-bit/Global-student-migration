import streamlit as st
from common import get_data

st.title("🗂️ Raw Data")

df = get_data()

st.dataframe(df, use_container_width=True)
st.caption(f"{len(df):,} rows × {df.shape[1]} columns")

csv = df.to_csv(index=False).encode("utf-8")
st.download_button("Download data as CSV", csv, file_name="global_student_migration.csv", mime="text/csv")