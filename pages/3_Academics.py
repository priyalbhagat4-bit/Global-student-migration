import plotly.express as px
import streamlit as st
from common import get_data

st.title("🎓 Academics")

df = get_data()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Scholarship Distribution")
    sch_count = df["scholarship_received"].value_counts()
    fig = px.pie(values=sch_count.values, names=sch_count.index, hole=0.45,
                 color_discrete_sequence=px.colors.qualitative.Set2)
    fig.update_traces(textinfo="percent+label")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Degree Distribution")
    degree_count = df["course_name"].value_counts()
    fig = px.pie(values=degree_count.values, names=degree_count.index, hole=0.3)
    fig.update_traces(textinfo="percent+label")
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Reasons for Enrollment")
if "enrollment_reason" in df.columns:
    top_reason = df["enrollment_reason"].value_counts().head(10)
    fig = px.line(x=top_reason.index, y=top_reason.values, markers=True,
                   labels={"x": "Enrollment reason", "y": "Number of students"})
    fig.update_traces(line_color="darkgreen")
    fig.update_xaxes(tickangle=45)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("`enrollment_reason` column not available.")

st.subheader("Test Score Distribution")
fig = px.histogram(df, x="test_score", nbins=10, marginal="box",
                    color_discrete_sequence=["#e63946"])
st.plotly_chart(fig, use_container_width=True)