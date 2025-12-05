"""
Data utilities module for Week 4 Coding Exercise.

This module provides utility functions for data manipulation and analysis
using pandas. It demonstrates proper module organization following PEP-8.
"""

import pandas as pd
import numpy as np


def load_data(filepath):
    """
    Load data from a CSV file.

    Parameters
    ----------
    filepath : str
        Path to the CSV file to load.

    Returns
    -------
    pd.DataFrame
        DataFrame containing the loaded data.

    Examples
    --------
    >>> df = load_data('data.csv')
    >>> print(df.head())
    """
    try:
        data = pd.read_csv(filepath)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File {filepath} not found.")
    except pd.errors.ParserError:
        raise ValueError(f"Error parsing CSV file: {filepath}")


def clean_data(df):
    """
    Clean data by removing duplicates and handling missing values.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame to clean.

    Returns
    -------
    pd.DataFrame
        Cleaned DataFrame with duplicates removed and NaN values handled.

    Examples
    --------
    >>> df_clean = clean_data(df)
    >>> print(df_clean.info())
    """
    df_clean = df.drop_duplicates()
    df_clean = df_clean.dropna()
    return df_clean


def summarize_data(df):
    """
    Generate summary statistics for a DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame to summarize.

    Returns
    -------
    dict
        Dictionary containing summary statistics.

    Examples
    --------
    >>> summary = summarize_data(df)
    >>> print(summary)
    """
    summary = {
        'rows': len(df),
        'columns': len(df.columns),
        'missing_values': df.isnull().sum().sum(),
        'dtypes': df.dtypes.to_dict(),
        'numeric_stats': df.describe().to_dict()
    }
    return summary


def filter_data(df, column, value):
    """
    Filter DataFrame by a specific column value.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame to filter.
    column : str
        Column name to filter by.
    value : any
        Value to filter for.

    Returns
    -------
    pd.DataFrame
        Filtered DataFrame.

    Examples
    --------
    >>> filtered_df = filter_data(df, 'category', 'A')
    >>> print(filtered_df)
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame.")
    return df[df[column] == value]


def aggregate_data(df, group_col, agg_col, agg_func='mean'):
    """
    Aggregate data by grouping on one column.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame to aggregate.
    group_col : str
        Column to group by.
    agg_col : str
        Column to aggregate.
    agg_func : str, default='mean'
        Aggregation function ('mean', 'sum', 'count', 'min', 'max').

    Returns
    -------
    pd.Series
        Aggregated data.

    Examples
    --------
    >>> result = aggregate_data(df, 'category', 'value', 'sum')
    >>> print(result)
    """
    valid_funcs = ['mean', 'sum', 'count', 'min', 'max']
    if agg_func not in valid_funcs:
        raise ValueError(f"agg_func must be one of {valid_funcs}")

    return df.groupby(group_col)[agg_col].agg(agg_func)


def create_sample_data(n_rows=100):
    """
    Create a sample DataFrame for testing and demonstration.

    Parameters
    ----------
    n_rows : int, default=100
        Number of rows to generate.

    Returns
    -------
    pd.DataFrame
        Sample DataFrame with synthetic data.

    Examples
    --------
    >>> sample_df = create_sample_data(50)
    >>> print(sample_df.head())
    """
    np.random.seed(42)
    categories = ['A', 'B', 'C']
    data = {
        'category': np.random.choice(categories, n_rows),
        'value': np.random.normal(100, 15, n_rows),
        'count': np.random.randint(1, 100, n_rows)
    }
    return pd.DataFrame(data)
