#!/usr/bin/env python3
"""
This module contains the function prune.
"""


def prune(df):
    """
    Remove rows where the Close column has NaN values.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: DataFrame with NaN values in Close removed.
    """
    return df.dropna(subset=["Close"])
