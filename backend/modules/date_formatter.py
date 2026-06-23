import pandas as pd

def standardize_dates(df, config):

    column = config.get("column", "data")

    df[column] = pd.to_datetime(df[column], errors="coerce")

    df[column] = df[column].dt.strftime("%Y-%m-%d")

    return df