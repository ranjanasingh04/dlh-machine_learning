#!/usr/bin/env python3
"""
This module contains a function that renames the Timestamp
column and converts it to datetime.
"""

import pandas as pd


def rename(df):
    """
    Renames the Timestamp column to Datetime,
    converts timestamps to datetime values,
    and returns only the Datetime and Close columns.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: Modified DataFrame.
    """
    df = df.rename(columns={"Timestamp": "Datetime"})
    df["Datetime"] = pd.to_datetime(df["Datetime"], unit="s")
    return df[["Datetime", "Close"]]
