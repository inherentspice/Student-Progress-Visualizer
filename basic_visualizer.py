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

# initialize figure
fig, ax = plt.subplots()

# create scatter plot with 'name' on the x-axis, and the results of the
# speaking test on the y-axis. The colour can be changed by writing in
# a different colour in quotes.
ax.scatter(pd1["Name"], pd1["Speaking"], color='lime', s=200, marker = 'o')

# the names on the axis are rotated so they do not blur together.
plt.xticks(rotation=45)

# set the x-axis label, y-axis label, and the figure label
plt.xlabel('Student name')
plt.ylabel('Questions answered correctly')
plt.ylim(0, 30)
plt.title('Speaking assessment')

# show the graph
plt.show()