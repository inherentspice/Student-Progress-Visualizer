# import packages: pandas to work with tabular data, matplotlib.pyplot to visualize data,
# seaborn to easily visualize data

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# import test data using pandas .read_csv()
semester_one_begin = pd.read_csv(r"progress_test_data_begin_sem_1.csv", index_col="Name")
semester_one_end = pd.read_csv(r"progress_test_data_end_sem_1.csv", index_col="Name")

# don't want the total_score row in the figure, so we drop it from the
# Dataframe using .drop()
pd1 = semester_one_begin.drop(semester_one_begin.index[-1])
pd2 = semester_one_end.drop(semester_one_end.index[-1])

# merge the two dataframes so they can be visualized easily
merged = pd1.merge(pd2, on="Name", how="outer", suffixes=("_begin", "_end"))

# use .columns to check the suffix names are correct
print(merged.columns)

# create dataframes seperated into categories
trans = merged[["Transcription_begin", "Transcription_end"]].copy()
writing = merged[["Writing Speed (Two Minutes)_begin", "Writing Speed (Two Minutes)_end"]].copy()
reading = merged[["Reading_begin", "Reading_end"]].copy()
sight = merged[["Sight Words_begin", "Sight Words_end"]].copy()
speak = merged[["Speaking_begin", "Speaking_end"]].copy()

#test visualization
g = speak.plot.bar()
g.set(xlabel="Student Results", ylabel="Speaking score out of 30")
plt.xticks(rotation=90)
plt.show()
