#!/usr/bin/env python3
"""
This module contains the function array.
"""


def array(df):
    """
    Select the last 10 rows of the High and Close columns
    and return them as a NumPy array.
    """
    return df[["High", "Close"]].tail(10).to_numpy()
