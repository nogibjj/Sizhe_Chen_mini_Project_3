import pytest
from mylib.lib import (
    load_dataset,
    general_describe,
    generate_vis,
    generate_dist,
    visualize_boxplot,
)

@pytest.fixture
def dataset():
    """
    Load the dataset to be used in multiple tests.
    """
    dataset_path = "StudentPerformanceFactors.csv"
    return load_dataset(dataset_path)


def test_load_dataset(dataset):
    """
    Test if the dataset is loaded correctly.
    """
    assert not dataset.empty, "The DataFrame should not be empty"

    expected_columns = ["Hours_Studied", "Exam_Score"]  # Replace with actual columns
    for col in expected_columns:
        assert col in dataset.columns, f"Column {col} should be in the DataFrame"


def test_general_describe(dataset):
    """
    Test the general_describe function.
    """
    column_to_analyze = "Hours_Studied"
    summary_stats = general_describe(dataset, column_to_analyze)

    # Ensure stats include mean, std, min, max, etc.
    expected_stats = ["mean", "std", "min", "max", "25%", "50%", "75%"]
    for stat in expected_stats:
        assert stat in summary_stats, f"Statistic {stat} should be in the summary"


def test_generate_vis(dataset):
    """
    Test the generate_vis function.
    """
    # Test to ensure no exceptions are raised
    generate_vis(dataset, "Hours_Studied", "Exam_Score", show=False)


def test_generate_dist(dataset):
    """
    Test the generate_dist function.
    """
    generate_dist(dataset, "Hours_Studied")


def test_visualize_boxplot(dataset):
    """
    Test the visualize_boxplot function.
    """
    visualize_boxplot(dataset, "Hours_Studied")