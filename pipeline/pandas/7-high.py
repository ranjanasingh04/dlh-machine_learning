#!/usr/bin/env python3
"""
This module contains the function high.
"""


def high(df):
    """
    Sort the DataFrame by the High column in descending order.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: Sorted DataFrame.
    """
    return df.sort_values(by="High", ascending=False)
