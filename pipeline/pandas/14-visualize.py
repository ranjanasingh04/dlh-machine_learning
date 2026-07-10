#!/usr/bin/env python3
"""
Visualize Bitcoin trading data at daily intervals.

The script cleans the Coinbase dataset, converts Unix timestamps to
datetime values, fills missing values, groups the data by day, and
plots the transformed DataFrame.
"""

import matplotlib.pyplot as plt
import pandas as pd

from_file = __import__('2-from_file').from_file


def visualize(df):
    """
    Clean, transform, resample, and visualize Bitcoin trading data.

    The function:
        - Removes the Weighted_Price column.
        - Renames Timestamp to Date.
        - Converts Unix timestamps to datetime values.
        - Sets Date as the DataFrame index.
        - Fills missing Close values using forward fill.
        - Fills missing High, Low, and Open values using Close.
        - Fills missing volume values with 0.
        - Keeps data from 2017 onwards.
        - Groups the data into daily intervals.
        - Plots the transformed data.

    Args:
        df (pd.DataFrame): DataFrame containing Bitcoin trading data.

    Returns:
        pd.DataFrame: Cleaned and daily-resampled DataFrame.
    """
    # Remove the Weighted_Price column
    df = df.drop(columns=["Weighted_Price"])

    # Rename Timestamp to Date
    df = df.rename(columns={"Timestamp": "Date"})

    # Convert Unix timestamps, measured in seconds, to datetime values
    df["Date"] = pd.to_datetime(df["Date"], unit="s")

    # Set Date as the DataFrame index
    df = df.set_index("Date")

    # Fill missing Close values with the previous valid value
    df["Close"] = df["Close"].ffill()

    # Fill missing High, Low, and Open values with Close
    for column in ["High", "Low", "Open"]:
        df[column] = df[column].fillna(df["Close"])

    # Fill missing volume values with zero
    volume_columns = ["Volume_(BTC)", "Volume_(Currency)"]
    df[volume_columns] = df[volume_columns].fillna(0)

    # Keep data from 2017 onwards
    df = df.loc["2017-01-01":]

    # Group values into daily intervals
    aggregation = {
        "High": "max",
        "Low": "min",
        "Open": "mean",
        "Close": "mean",
        "Volume_(BTC)": "sum",
        "Volume_(Currency)": "sum"
    }

    df = df.resample("D").agg(aggregation)

    # Plot the transformed DataFrame
    df.plot(figsize=(12, 8))
    plt.title("Daily Bitcoin Trading Data from 2017")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.tight_layout()
    plt.show()

    return df


df = from_file(
    "coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv",
    ","
)

transformed_df = visualize(df)
