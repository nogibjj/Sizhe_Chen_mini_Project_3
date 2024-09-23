from pyinstrument import Profiler
from mylib.lib import load_dataset, general_describe
from main import load_dataset_pl, general_describe_pl

dataset_path = "StudentPerformanceFactors.csv"

# Add a loop to increase the profiling duration
with Profiler(interval=0.1) as profiler_pandas:
    df_pandas = load_dataset(dataset_path)
    stats_pandas = general_describe(df_pandas, "Hours_Studied")
    print(stats_pandas)

profiler_pandas.print()

with Profiler(interval=0.1) as profiler_polars:
    df_polars = load_dataset_pl(dataset_path)
    stats_polars = general_describe_pl(df_polars, "Hours_Studied")
    print(stats_polars)

profiler_polars.print()
