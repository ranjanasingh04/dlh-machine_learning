#!/usr/bin/env python3
"""
This module contains the function flip_switch.
"""


def flip_switch(df):
    """
    Sort the DataFrame in reverse chronological order
    and transpose it.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: Transformed DataFrame.
    """
    return df.iloc[::-1].transpose()
