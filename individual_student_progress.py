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

#initialize the matplotlib figure
f, ax = plt.subplots(figsize=(6, 15))

# set color palette
sns.set_color_codes("deep")

# plot the end of semester one results first
sns.barplot(x=merged.index, y="Transcription_end", data=merged,
            label="January, 2022", color="b")

# set color of September plot
sns.set_color_codes("bright")

# plot the beginning of semester one results
sns.barplot(x=merged.index, y="Transcription_begin", data=merged,
            label="September, 2021", color="r")

# rotate xticks so they are readable
plt.xticks(rotation=90)

plt.show()
