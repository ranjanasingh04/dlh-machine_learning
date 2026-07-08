#!/usr/bin/env python3
"""
This module contains the function index.
"""

def index(df):
    """
    Set the Timestamp column as the DataFrame index.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: Modified DataFrame.
    """
    return df.set_index("Timestamp")