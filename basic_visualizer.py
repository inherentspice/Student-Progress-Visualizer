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

# initialize the figure
fig, ax = plt.subplots()

# a function that takes the axes, the data to plot on the x-axis, the
# data to plot on the y-axis, the x-axis title, the y-axis table, the color
# of the bars, and the title of the graph

# def make_bar(axes, x, y, xlabel, ylabel, color, title):
#     ax.bar(x, y, color=color)
#     plt.xticks(rotation=45)
#     plt.xlabel(xlabel)
#     plt.ylabel(ylabel)
#     plt.ylim(0, (max(y)+2))
#     plt.title(label=title)
#
# # call make_bar function with student name on x-axis, score for writing text
# # on y-axis
# make_bar(ax, pd1["Name"], pd1["Writing Speed (Two Minutes)"], "Name of student", "Words written in two minutes", "purple", "Writing speed test")

ax.bar(pd1["Name"], pd1["Speaking"], color='blue')
plt.xticks(rotation=45)
ax2 = ax.twinx()
ax2.bar(pd2["Name"], pd2["Speaking"], color='red', alpha=0.3)
plt.ylim(0, (max(semester_one_begin["Speaking"])))
plt.xlabel("Student name")
plt.ylabel("Speaking score")
plt.title(label="Speaking Assessment")

# show graph
plt.show()
