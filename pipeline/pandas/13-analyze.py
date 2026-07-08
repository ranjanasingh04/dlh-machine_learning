#!/usr/bin/env python3
"""
Module that computes descriptive statistics for a DataFrame.
"""


def analyze(df):
    """
    Computes descriptive statistics for all columns except Timestamp.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: Descriptive statistics.
    """
    return df.drop(columns=["Timestamp"]).describe()
