import pandas as pd
import plotly.express as px
import streamlit as st
from common import get_data

st.title("🌍 Migration Patterns")

df = get_data()

top_n = st.slider("Top N countries to show", 5, 20, 10)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Top Destination Countries")
    top_dest = df["destination_country"].value_counts().head(top_n)
    fig = px.bar(
        x=top_dest.index, y=top_dest.values,
        labels={"x": "Country", "y": "Number of students"},
        color=top_dest.index, color_discrete_sequence=px.colors.sequential.Purples_r,
    )
    fig.update_layout(showlegend=False)
    fig.update_xaxes(tickangle=45)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Top Origin Countries")
    top_origin = df["origin_country"].value_counts().head(top_n)
    fig = px.bar(
        x=top_origin.index, y=top_origin.values,
        labels={"x": "Country", "y": "Number of students"},
        color=top_origin.index, color_discrete_sequence=px.colors.diverging.RdBu,
    )
    fig.update_layout(showlegend=False)
    fig.update_xaxes(tickangle=45)
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Students Growth Over the Years")
year_count = df["year_of_enrollment"].value_counts().sort_index()
fig = px.line(
    x=year_count.index, y=year_count.values, markers=True,
    labels={"x": "Year of enrollment", "y": "Number of students"},
)
fig.update_traces(line_color="teal")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Origin → Destination Flow")
cross = pd.crosstab(df["origin_country"], df["destination_country"])
fig = px.imshow(
    cross, text_auto="d", aspect="auto", color_continuous_scale="Spectral",
    labels=dict(x="Destination Country", y="Origin Country", color="Students"),
)
fig.update_layout(height=650)
st.plotly_chart(fig, use_container_width=True)