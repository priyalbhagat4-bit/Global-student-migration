import pandas as pd
import plotly.express as px
import streamlit as st
from common import get_data

st.title("💼 Career Outcomes")

df = get_data()

st.subheader("GPA vs Starting Salary")
fig = px.scatter(
    df, x="gpa_or_score", y="starting_salary_usd", color="placement_status",
    color_discrete_sequence=["#e89835", "#3287a8"], opacity=0.7,
    labels={"gpa_or_score": "GPA", "starting_salary_usd": "Starting Salary (USD)"},
)
st.plotly_chart(fig, use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Salary Distribution")
    fig = px.histogram(df, x="starting_salary_usd", nbins=20, marginal="box",
                        color_discrete_sequence=["orange"])
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Salary by Field of Study")
    avg_salary = (
        df.groupby("field_of_study")["starting_salary_usd"].mean()
        .sort_values(ascending=False).reset_index()
    )
    fig = px.bar(avg_salary, x="field_of_study", y="starting_salary_usd",
                 color_discrete_sequence=px.colors.qualitative.Set2)
    fig.update_xaxes(tickangle=45)
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Salary by Destination Country")
fig = px.box(df, x="destination_country", y="starting_salary_usd",
             color="destination_country", color_discrete_sequence=px.colors.qualitative.Set2)
fig.update_layout(showlegend=False)
fig.update_xaxes(tickangle=45)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Placements: Country vs Company")
placed = df.dropna(subset=["placement_country", "placement_company"])
if len(placed):
    cross = pd.crosstab(placed["placement_country"], placed["placement_company"])
    fig = px.imshow(cross, text_auto="d", aspect="auto", color_continuous_scale="YlGnBu",
                     labels=dict(x="Placement Company", y="Placement Country", color="Placements"))
    fig.update_layout(height=650)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No placement data available.")