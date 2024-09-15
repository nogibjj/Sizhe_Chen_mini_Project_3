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

def save_to_md():
    with open("test.md","a") as file:
        file.write("test")

if __name__ == "__main__":
    save_to_md()