import pandas as pd


def get_raw_data():
    """Get raw data from data/raw/ directory."""
    return pd.read_csv("data/raw/iris.csv")