#!/usr/bin/env python3
"""
Module that concatenates two DataFrames with hierarchical indexing.
"""

import pandas as pd
index = __import__('10-index').index


def hierarchy(df1, df2):
    """
    Concatenate bitstamp and coinbase data with Timestamp as first index level.
    """
    df1 = index(df1)
    df2 = index(df2)

    df1 = df1.loc[1417411980:1417417980]
    df2 = df2.loc[1417411980:1417417980]

    df = pd.concat(
        [df2, df1],
        keys=["bitstamp", "coinbase"]
    )

    df = df.swaplevel(0, 1)
    df = df.sort_index()

    return df
