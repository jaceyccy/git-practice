# Data cleaning script
import pandas as pd

THRESHOLD = 4.0


def load(path):
    return pd.read_csv(path)


def drop_missing(df):
    return df.dropna().reset_index(drop=True)


def remove_outliers(df, column):
    z = (df[column] - df[column].mean()) / df[column].std()
    return df[z.abs() <= THRESHOLD]
