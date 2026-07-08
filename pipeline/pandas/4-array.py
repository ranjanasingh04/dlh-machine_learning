#!/usr/bin/env python3
"""
This module create a function array(df)
that takes a pd.DataFrame
Returns: the numpy.ndarray
"""

import pandas as pd


def array(df):
    """
    function should select the last 10 rows of the High and Close columns.
    Convert these selected values into a numpy.ndarray.
    """
    columns = [{
        "High", "Low"
    }]
    return df[["High", "Low"]].tail(10).to_numpy()
