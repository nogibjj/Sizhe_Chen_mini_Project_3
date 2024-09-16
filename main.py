"""
Main Functions
"""
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset from a CSV file
def load_dataset(file_path):
    """
    Load dataset from a CSV file into a pandas DataFrame.
    
    Parameters:
        file_path (str): The path to the dataset file.
        
    Returns:
        pd.DataFrame: The loaded dataset.
    """
    dataframe = pd.read_csv(file_path)
    return dataframe

# Generate descriptive statistics for a specific column
def general_describe(dataframe, column_name):
    """
    Generate descriptive statistics for a specific column in the DataFrame.
    
    Parameters:
        dataframe (pd.DataFrame): The dataset.
        column_name (str): The name of the column to describe.
        
    Returns:
        pd.Series: Descriptive statistics for the specified column.
    """
    return dataframe[column_name].describe()

# Create a scatter plot for two variables
def generate_vis(dataframe, x_col, y_col):
    """
    Generate a scatter plot for two variables to visualize their relationship.
    
    Parameters:
        dataframe (pd.DataFrame): The dataset.
        x_col (str): The name of the X-axis column.
        y_col (str): The name of the Y-axis column.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(dataframe[x_col], dataframe[y_col], color='green', alpha=0.6)
    plt.title(f'{x_col} vs {y_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True)
    plt.show()

# Generate a histogram for a variable
def generate_dist(dataframe, column_name):
    """
    Generate a histogram to visualize the distribution of a variable.
    
    Parameters:
        dataframe (pd.DataFrame): The dataset.
        column_name (str): The name of the column to visualize.
    """
    plt.figure(figsize=(10, 6))
    plt.hist(dataframe[column_name], bins=15, color='green', edgecolor='black')
    plt.title(f'Distribution of {column_name}')
    plt.xlabel(column_name)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

# Create a boxplot for a variable
def visualize_boxplot(dataframe, column_name):
    """
    Generate a boxplot to summarize the distribution of a variable.
    
    Parameters:
        dataframe (pd.DataFrame): The dataset.
        column_name (str): The name of the column to visualize.
    """
    plt.boxplot(dataframe[column_name], vert=False, patch_artist=True, showmeans=True, 
                boxprops=dict(facecolor='lightcoral'), 
                flierprops=dict(markerfacecolor='green', marker='o'))

    plt.title(f'Box Plot of {column_name}')
    plt.xlabel(column_name)
    plt.grid(True)
    plt.show()

# Save summary statistics to a markdown file
def save_to_md(summary_stats, column_name):
    """
    Save the summary statistics of a column to a markdown (.md) file.
    
    Parameters:
        summary_stats (pd.Series): Descriptive statistics for the column.
        column_name (str): The name of the column.
    """
    with open("summary_statistics.md", "w", encoding="utf-8") as file:
        file.write(f"# Summary Statistics for {column_name}\n\n")
        file.write(f"**Mean**: {summary_stats['mean']}\n\n")
        file.write(f"**Median (50%)**: {summary_stats['50%']}\n\n")
        file.write(f"**Max**: {summary_stats['max']}\n\n")
        file.write(f"**Min**: {summary_stats['min']}\n\n")
        file.write(f"**Standard Deviation**: {summary_stats['std']}\n\n")
        file.write(f"**25th Percentile (25%)**: {summary_stats['25%']}\n\n")
        file.write(f"**75th Percentile (75%)**: {summary_stats['75%']}\n\n")

# Main execution
if __name__ == "__main__":
    dataset_path = "StudentPerformanceFactors.csv" 
    column_to_analyze = "Hours_Studied"  
    
    # Load dataset
    df = load_dataset(dataset_path)
    
    # Generate descriptive statistics for the specified column
    summary_stats = general_describe(df, column_to_analyze)
    
    # Save summary statistics to markdown file
    save_to_md(summary_stats, column_to_analyze)

