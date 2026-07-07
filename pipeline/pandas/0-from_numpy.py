#!/usr/bin/env python3
"""
This module contains a function that creates a pandas DataFrame
from a NumPy ndarray.
"""

import pandas as pd


def from_numpy(array):
    """
    Creates a pandas DataFrame from a NumPy array.

    Args:
        array (np.ndarray): NumPy array.

    Returns:
        pd.DataFrame: DataFrame with columns labeled A, B, C, ...
    """
    columns = [chr(65 + i) for i in range(array.shape[1])]
    return pd.DataFrame(array, columns=columns)
