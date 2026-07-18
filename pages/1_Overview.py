import streamlit as st
from common import get_data

st.title("🎓 Global Student Migration Dashboard")
st.markdown(
    "Trends in global student migration — popular destinations, fields of "
    "study, and outcomes after graduation."
)

df = get_data()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total students", f"{len(df):,}")
if "placement_status" in df.columns:
    col2.metric("Placement rate", f"{(df['placement_status'] == 'Placed').mean() * 100:.1f}%")
if "starting_salary_usd" in df.columns:
    placed_sal = df.loc[df["placement_status"] == "Placed", "starting_salary_usd"]
    col3.metric("Avg. starting salary (placed)", f"${placed_sal.mean():,.0f}")
if "scholarship_received" in df.columns:
    col4.metric("Scholarship rate", f"{(df['scholarship_received'] == 'Yes').mean() * 100:.1f}%")

st.markdown("---")

c1, c2 = st.columns([2, 1])
with c1:
    st.subheader("What's in this dashboard")
    st.markdown(
        """
- **Migration Patterns** — top destinations, top origins, enrollment growth, and origin→destination flow
- **Academics** — scholarships, degrees, enrollment reasons, and test scores
- **Career Outcomes** — GPA vs. salary, salary distributions, and placements
- **Raw Data** — the full dataset and a CSV download
"""
    )
with c2:
    st.subheader("Dataset")
    st.write(f"**Rows:** {df.shape[0]:,}")
    st.write(f"**Columns:** {df.shape[1]}")
    st.write(f"**Duplicate rows:** {df.duplicated().sum()}")

with st.expander("Missing values by column"):
    st.dataframe(df.isnull().sum().rename("missing_count").to_frame(), use_container_width=True)