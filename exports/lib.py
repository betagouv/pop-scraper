import pandas as pd

def load_export_df(csv_path):
    df = pd.read_csv(csv_path, dtype={"DPT": str})
    df.drop(columns=["key"], inplace=True)
    return df