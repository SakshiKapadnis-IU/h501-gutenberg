"""
Visualization module for Week 4 Coding Exercise.

This module provides utility functions for data visualization
using Seaborn. It demonstrates proper module organization and
integration with pandas DataFrames.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def setup_style():
    """
    Set up Seaborn style for consistent visualizations.

    This function sets the Seaborn style to 'darkgrid' and
    increases the figure size for better readability.

    Examples
    --------
    >>> setup_style()
    """
    sns.set_style("darkgrid")
    plt.rcParams['figure.figsize'] = (12, 6)


def plot_distribution(data, column, title=None, bins=30):
    """
    Create a distribution plot for a single column.

    Parameters
    ----------
    data : pd.DataFrame
        DataFrame containing the data.
    column : str
        Column name to plot.
    title : str, optional
        Title for the plot. If None, uses column name.
    bins : int, default=30
        Number of bins for the histogram.

    Returns
    -------
    matplotlib.axes.Axes
        The axes object containing the plot.

    Examples
    --------
    >>> ax = plot_distribution(df, 'value', title='Value Distribution')
    >>> plt.show()
    """
    if column not in data.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame.")

    if title is None:
        title = f"Distribution of {column}"

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(data=data, x=column, bins=bins, kde=True, ax=ax)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel(column, fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)
    plt.tight_layout()
    return ax


def plot_scatter(data, x, y, hue=None, title=None):
    """
    Create a scatter plot for two columns.

    Parameters
    ----------
    data : pd.DataFrame
        DataFrame containing the data.
    x : str
        Column name for x-axis.
    y : str
        Column name for y-axis.
    hue : str, optional
        Column name for color encoding.
    title : str, optional
        Title for the plot.

    Returns
    -------
    matplotlib.axes.Axes
        The axes object containing the plot.

    Examples
    --------
    >>> ax = plot_scatter(df, 'value', 'count', hue='category')
    >>> plt.show()
    """
    for col in [x, y]:
        if col not in data.columns:
            raise ValueError(f"Column '{col}' not found in DataFrame.")

    if hue and hue not in data.columns:
        raise ValueError(f"Column '{hue}' not found in DataFrame.")

    if title is None:
        title = f"{y} vs {x}"

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=data, x=x, y=y, hue=hue, ax=ax, s=100)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel(x, fontsize=12)
    ax.set_ylabel(y, fontsize=12)
    plt.tight_layout()
    return ax


def plot_boxplot(data, x=None, y=None, title=None):
    """
    Create a box plot to show distribution by category.

    Parameters
    ----------
    data : pd.DataFrame
        DataFrame containing the data.
    x : str, optional
        Column name for x-axis (categorical).
    y : str, optional
        Column name for y-axis (numeric).
    title : str, optional
        Title for the plot.

    Returns
    -------
    matplotlib.axes.Axes
        The axes object containing the plot.

    Examples
    --------
    >>> ax = plot_boxplot(df, x='category', y='value')
    >>> plt.show()
    """
    if x and x not in data.columns:
        raise ValueError(f"Column '{x}' not found in DataFrame.")
    if y and y not in data.columns:
        raise ValueError(f"Column '{y}' not found in DataFrame.")

    if title is None:
        title = f"{y} by {x}" if x else f"Box Plot of {y}"

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=data, x=x, y=y, ax=ax)
    ax.set_title(title, fontsize=14, fontweight='bold')
    if x:
        ax.set_xlabel(x, fontsize=12)
    if y:
        ax.set_ylabel(y, fontsize=12)
    plt.tight_layout()
    return ax


def plot_heatmap(data, title=None, cmap='coolwarm'):
    """
    Create a correlation heatmap for numeric columns.

    Parameters
    ----------
    data : pd.DataFrame
        DataFrame containing the data.
    title : str, optional
        Title for the plot.
    cmap : str, default='coolwarm'
        Colormap for the heatmap.

    Returns
    -------
    matplotlib.axes.Axes
        The axes object containing the plot.

    Examples
    --------
    >>> ax = plot_heatmap(df, title='Correlation Matrix')
    >>> plt.show()
    """
    if title is None:
        title = "Correlation Heatmap"

    corr_matrix = data.corr(numeric_only=True)
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap=cmap, ax=ax,
                cbar_kws={'label': 'Correlation'})
    ax.set_title(title, fontsize=14, fontweight='bold')
    plt.tight_layout()
    return ax


def plot_categorical(data, column, title=None, orient='v'):
    """
    Create a categorical count plot.

    Parameters
    ----------
    data : pd.DataFrame
        DataFrame containing the data.
    column : str
        Column name to plot.
    title : str, optional
        Title for the plot.
    orient : str, default='v'
        Orientation of the plot ('v' for vertical, 'h' for horizontal).

    Returns
    -------
    matplotlib.axes.Axes
        The axes object containing the plot.

    Examples
    --------
    >>> ax = plot_categorical(df, 'category', title='Category Counts')
    >>> plt.show()
    """
    if column not in data.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame.")

    if title is None:
        title = f"Counts of {column}"

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(data=data, x=column if orient == 'v' else None,
                  y=column if orient == 'h' else None, ax=ax)
    ax.set_title(title, fontsize=14, fontweight='bold')
    plt.tight_layout()
    return ax
