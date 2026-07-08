#!/usr/bin/env python3
"""
This module contains the function slice.
"""


def slice(df):
    """
    Selects every 60th row from these columns.
    and return the sliced pd.DataFrame
    """
    return df[["High", "Low", "Close", "Volume_(BTC)"]].iloc[::60]
