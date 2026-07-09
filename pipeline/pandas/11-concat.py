#!/usr/bin/env python3
"""
Module that concatenates two DataFrames.
"""
import pandas as pd
index = __import__('10-index').index


def concat(df1, df2):
    """
    Concatenate df2 (bitstamp) above df1 (coinbase).

    Args:
        df1 (pd.DataFrame): Coinbase DataFrame.
        df2 (pd.DataFrame): Bitstamp DataFrame.

    Returns:
        pd.DataFrame: Concatenated DataFrame.
    """
    # Set Timestamp as the index
    df1 = index(df1)
    df2 = index(df2)

    # Keep timestamps up to and including 1417411920
    df2 = df2.loc[:1417411920]

    # Concatenate with keys
    concat_df = pd.concat(
        [df2, df1],
        keys=["bitstamp", "coinbase"]
    )
    return concat_df
