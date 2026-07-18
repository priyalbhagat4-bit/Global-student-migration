"""Shared utilities for the Global Student Migration dashboard."""

import os
import pandas as pd
import streamlit as st

# Path to the dataset, relative to this file's folder (common.py).
# Change this single line if your CSV lives somewhere else.
CSV_PATH = os.path.join(os.path.dirname(__file__), "data", "global_student_migration dataset.csv")


@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def get_data() -> pd.DataFrame:
    """Reads the CSV directly from CSV_PATH. No upload, no session_state needed."""
    return load_data(CSV_PATH)