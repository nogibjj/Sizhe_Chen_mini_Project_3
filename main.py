"""
Main Functions
"""
import pandas as pd
import matplotlib.pyplot as plt


def load_dataset(dataset):
    df = pd.read_csv(dataset)
    return df

def general_describe(df,col):
    return df[col].describe()

def generate_vis(df,x1,x2):
    "generate the scattar plot of two variables to see their relationship"
    plt.figure(figsize=(10, 6))
    plt.scatter(df[x1], df[x2], color='green', alpha=0.6)
    plt.title(f'{x1} vs {x2}')
    plt.xlabel(x1)
    plt.ylabel(x2)
    plt.grid(True)
    plt.show()

def generate_dist(df,x):
    "generate the distribution of the variable"
    plt.figure(figsize=(10, 6))
    plt.hist(df[x], bins=15, color='green', edgecolor='black')
    plt.title(f'Distribution of {x}')
    plt.xlabel(x)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

def visualize_boxplot(df, column):
    "build a boxplot"
    plt.boxplot(df[column], vert=False, patch_artist=True, showmeans=True, 
                boxprops=dict(facecolor='lightcoral'), 
                flierprops=dict(markerfacecolor='green', marker='o'))

    plt.title(f'Box Plot of {column}')
    plt.xlabel(column)
    plt.grid(True)
    plt.show()

def save_to_md(summary, column_name):
    with open("summary_statistics.md", "w", encoding="utf-8") as file:
        file.write(f"# Summary Statistics for {column_name}\n\n")
        file.write(f"**Mean**: {summary['mean']}\n\n")
        file.write(f"**Median (50%)**: {summary['50%']}\n\n")
        file.write(f"**Max**: {summary['max']}\n\n")
        file.write(f"**Min**: {summary['min']}\n\n")
        file.write(f"**Standard Deviation**: {summary['std']}\n\n")
        file.write(f"**25th Percentile (25%)**: {summary['25%']}\n\n")
        file.write(f"**75th Percentile (75%)**: {summary['75%']}\n\n")

if __name__ == "__main__":
    dataset = "StudentPerformanceFactors.csv"
    column_name = "Hours_Studied"
    
    df = load_dataset(dataset)
    summary = general_describe(df, column_name)
    
    save_to_md(summary, column_name)