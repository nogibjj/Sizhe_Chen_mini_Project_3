"""
Test goes here

"""

from main import (
    load_dataset_pl, 
    general_describe_pl, 
    generate_vis_pl, 
    generate_dist_pl, 
    visualize_boxplot_pl
)

dataset = "./StudentPerformanceFactors.csv"

df = load_dataset_pl(dataset)

# Test the general_describe function for 'Hours_Studied'
def test_general_describe():
    desc = general_describe_pl(df, 'Hours_Studied')
    assert round(desc['mean'][0], 6) == 19.975329
    assert desc['median'][0] == 20.0
    assert desc['max'][0] == 44.0 
    assert desc['min'][0] == 1.0
    assert round(desc['std'][0], 6) == 5.990594 
    assert desc['25%'][0] == 16.0
    assert desc['75%'][0] == 24.0


# Test the generate_vis function for 'Hours_Studied' vs 'Exam_Score'
def test_generate_vis():
    try:
        generate_vis_pl(df, 'Hours_Studied', 'Exam_Score')
    except Exception as e:
        assert False, f"generate_vis raised an exception: {e}"

# Test the generate_dist function for 'Hours_Studied'
def test_generate_dist():
    try:
        generate_dist_pl(df, 'Hours_Studied')
    except Exception as e:
        assert False, f"generate_dist raised an exception: {e}"

# Test the visualize_boxplot function for 'Hours_Studied'
def test_visualize_boxplot():
    try:
        visualize_boxplot_pl(df, 'Hours_Studied')
    except Exception as e:
        assert False, f"visualize_boxplot raised an exception: {e}"

# Run the tests
if __name__ == "__main__":
    test_general_describe()
    test_generate_vis()
    test_generate_dist()
    test_visualize_boxplot()
    print("All tests passed.")
