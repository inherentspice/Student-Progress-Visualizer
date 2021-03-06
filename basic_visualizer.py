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
# data to plot on the y-axis, the x-axis title, the y-axis title, the title of the graph,
# and the name of the file you want created

def class_bar(ax, x_axis, y_axis_one, y_axis_two, xlabel, ylabel, title, file_name):
    ax.bar(x_axis, y_axis_one, color='blue')
    plt.xlabel(xlabel, fontsize=18)
    plt.ylabel(ylabel, fontsize=18)
    plt.title(title, fontsize=20)

# set_xticks with no value in square brackets will give
# no names on the x-axis. Update this later so only the
# one student name is shown.

    ax.set_xticks([])
    plt.ylim(0, (max(y_axis_two)))
    ax2 = ax.twinx()
    ax2.bar(x_axis, y_axis_two, color='red', alpha=0.3)
    plt.tight_layout()
    # save figure as pdf
    plt.savefig(file_name)





# delete hashtag on lines below to generate pdf of each figure

# class_bar(ax, pd1["Name"], pd1["Writing Speed (Two Minutes)"], pd2["Writing Speed (Two Minutes)"], "Name of student", "Words written in two minutes", "Writing speed test", "writing_bar.pdf")
# class_bar(ax, pd1["Name"], pd1["Transcription"], pd2["Transcription"], "Name of student", "Words transcribed correctly", "Transcription test", "transcription_bar.pdf")
# class_bar(ax, pd1["Name"], pd1["Speaking"], pd2["Speaking"], "Name of student", "Questions answered with correct grammar", "Speaking test", "speaking_bar.pdf")
# class_bar(ax, pd1["Name"], pd1["Sight Words"], pd2["Sight Words"], "Name of student", "Sight words read correctly", "Sight words test", "sight_words_bar.pdf")
# class_bar(ax, pd1["Name"], pd1["Reading"], pd2["Reading"], "Name of student", "Words read correctly", "Reading test", "reading_bar.pdf")