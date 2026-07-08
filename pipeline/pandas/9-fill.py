#!/usr/bin/env python3
"""
This module contains the function fill.
"""


def fill(df):
    """
    Modify the DataFrame by:
    - Removing the Weighted_Price column.
    - Filling missing Close values with the previous value.
    - Filling missing High, Low, and Open values with Close.
    - Filling missing Volume_(BTC) and Volume_(Currency) values with 0.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: Modified DataFrame.
    """
    # Remove the Weighted_Price column
    df = df.drop(columns=["Weighted_Price"])

    # Fill missing Close values with the previous row's value
    df["Close"] = df["Close"].fillna(method="ffill")

    # Fill missing High, Low, and Open values with Close
    df["High"] = df["High"].fillna(df["Close"])
    df["Low"] = df["Low"].fillna(df["Close"])
    df["Open"] = df["Open"].fillna(df["Close"])

    # Fill missing volume values with 0
    df["Volume_(BTC)"] = df["Volume_(BTC)"].fillna(0)
    df["Volume_(Currency)"] = df["Volume_(Currency)"].fillna(0)

    return df
