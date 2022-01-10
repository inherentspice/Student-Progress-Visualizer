# import packages: pandas to work with tabular data, matplotlib.pyplot to visualize data

import pandas as pd
import matplotlib.pyplot as plt

# import test data using pandas .read_csv()
semester_one_begin = pd.read_csv(r"progress_test_data_begin_sem_1.csv")
semester_one_end = pd.read_csv(r"progress_test_data_end_sem_1.csv")

# check that there were no problems converting csv to dataframes
print(semester_one_begin.head())
print(semester_one_end.head())

# don't want the total_score row in the figure, so we drop it from the
# Dataframe using .drop()
pd1 = semester_one_begin.drop(semester_one_begin.index[-1])
pd2 = semester_one_end.drop(semester_one_end.index[-1])

