import pandas as pd
import matplotlib.pyplot as plt


def load_dataset(file_path):
    dataframe = pd.read_csv(file_path)
    return dataframe


def general_describe(dataframe, column_name):
    """
    Generate descriptive statistics for a specific column in the DataFrame.
    """
    return dataframe[column_name].describe()


def generate_vis(dataframe, x_col, y_col, show=True):
    """
    Generate a scatter plot for two variables to visualize their relationship.
    Optionally, display or suppress the plot.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(dataframe[x_col], dataframe[y_col], color="green", alpha=0.6)
    plt.title(f"{x_col} vs {y_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True)

    if show:
        plt.show()


def generate_dist(dataframe, column_name, show=True):
    """
    Generate a histogram to visualize the distribution of a variable.
    """
    plt.figure(figsize=(10, 6))
    plt.hist(dataframe[column_name], bins=15, color="green", edgecolor="black")
    plt.title(f"Distribution of {column_name}")
    plt.xlabel(column_name)
    plt.ylabel("Frequency")
    plt.grid(True)
    if show:
        plt.show()


def visualize_boxplot(dataframe, column_name, show=True):
    """
    Generate a boxplot to summarize the distribution of a variable.
    """
    plt.boxplot(
        dataframe[column_name],
        vert=False,
        patch_artist=True,
        showmeans=True,
        boxprops=dict(facecolor="lightcoral"),
        flierprops=dict(markerfacecolor="green", marker="o"),
    )

    plt.title(f"Box Plot of {column_name}")
    plt.xlabel(column_name)
    plt.grid(True)
    if show:
        plt.show()