#!/usr/bin/env python3
"""
This module contains a function that loads data from a file
into a pandas DataFrame.
"""

import pandas as pd


def from_file(filename, delimiter):
    """
    Loads data from a file as a pandas DataFrame.

    Args:
        filename: Name of the file to load.
        delimiter: Column separator used in the file.

    Returns:
        A pandas DataFrame.
    """
    return pd.read_csv(filename, sep=delimiter)
