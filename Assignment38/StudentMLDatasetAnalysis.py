'''
Dataset Description – Student Performance ML
Dataset
The dataset student_performance_ml.csv contains academic and behavioral information of
students. The objective of this dataset is to predict whether a student will Pass (1) or Fail (0) based on various
input features.
Each row in the dataset represents one student, and each column represents a measurable factor that may
influence academic performance.
Features Description
• StudyHours – Number of hours a student studies per day.
• Attendance – Percentage of class attendance.
• PreviousScore – Marks obtained in the previous examination.
• AssignmentsCompleted – Number of assignments completed by the student.
• SleepHours – Average number of hours the student sleeps per day.
• FinalResult – Target variable (Output):
◦ 1 → Pass
◦ 0 → Fail

Objective of the Dataset
The goal is to:
• Analyze how different factors affect student performance.
• Build a Machine Learning model to predict whether a student will pass or fail.
• Understand concepts such as training, testing, accuracy, confusion matrix, overfitting, and model
evaluation.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

'''
1. Write a Python program to load the file student_performance_ml.csv using pandas.
Display:
• First 5 records
• Last 5 records
• Total number of rows and columns
• List of column names
• Data types of each column
'''
#Read the Dataset
data = pd.read_csv("student_performance_ml.csv")

# Display the first few rows of the dataset
print(data.head())

#Display the last few rows of the dataset
print(data.tail())

#Display the shape of the dataset
print("Shape of the dataset:", data.shape)
print("Total Rows: ", data.shape[0])
print("Total Columns: ", data.shape[1])

#Display the data types of each column
print("Data types of each column:\n", data.dtypes)

#Display the summary statistics of the dataset
print(data.describe())

#Display columns in the dataset
print("Columns in the dataset:", data.columns)

#Display the number of missing values in each column
print("Missing values in each column:\n", data.isnull().sum())

#Display the distribution of the target variable
print("Distribution of FinalResult:\n", data['FinalResult'].value_counts())

'''
2. Write a program to:
• Display total number of students in the dataset
• Count how many students Passed (FinalResult = 1)
• Count how many students Failed (FinalResult = 0)
'''
#Display the distribution of the target variable
print("Distribution of FinalResult:\n", data['FinalResult'].value_counts())

print('Total number of students in the dataset: ', data.shape[0])
print('Number of students who Passed (FinalResult = 1): ', data[data['FinalResult'] == 1].shape[0])
print('Number of students who Failed (FinalResult = 0): ', data[data['FinalResult'] == 0].shape[0])

'''
3. Using pandas functions, calculate and display:
• Average StudyHours
• Average Attendance
• Maximum PreviousScore
• Minimum SleepHours
'''
#Average StudyHours
print("Average StudyHours: ", data['StudyHours'].mean())

#Average Attendance
print("Average Attendance: ", data['Attendance'].mean())

#Maximum PreviousScore
print("Maximum PreviousScore: ", data['PreviousScore'].max())

#Minimum SleepHours
print("Minimum SleepHours: ", data['SleepHours'].min())

'''
4. Use value_counts() to analyze the distribution of FinalResult.
Calculate the percentage of Pass and Fail students.
Is the dataset balanced? Justify your answer.
'''

#percentage of Pass and Fail students
final_result_counts = data['FinalResult'].value_counts()
total_students = data.shape[0]
pass_percentage = (final_result_counts[1] / total_students) * 100
fail_percentage = (final_result_counts[0] / total_students) * 100

print("Percentage of Pass students: ", pass_percentage)
print("Percentage of Fail students: ", fail_percentage)

'''
5. Based on the dataset values, analyze whether:
• Higher StudyHours increase the chance of passing.
• Higher Attendance improves FinalResult.
Write your observations in 4–5 lines.
'''

# For checking down the relationship between StudyHours and Attendance with FinalResult, we can check the correlation values
#  between these features and the target variable. We can also visualize the relationships using scatter plots or 
#  box plots. 

print("Correlation between StudyHours and FinalResult: \n", data['StudyHours'].corr(data['FinalResult'])) #0.85

print("Correlation between Attendance and FinalResult: \n", data['Attendance'].corr(data['FinalResult'])) #0.85

"""
Observations:
1. There is a strong positive correlation between StudyHours and FinalResult.
2. There is a strong positive correlation between Attendance and FinalResult.
3. Students who study more hours and have higher attendance are more likely to pass.
4. These observations suggest that both StudyHours and Attendance are important factors influencing student performance.

"""


'''
6. Plot a histogram of StudyHours.
Explain what the distribution tells you.
'''

# Plotting a histogram of StudyHours
plt.hist(data['StudyHours'], bins=10, edgecolor='black')
plt.title('Distribution of StudyHours')
plt.xlabel('StudyHours')
plt.ylabel('Frequency')
plt.savefig('study_hours_histogram.png')  # Save the histogram as an image file
plt.show()

'''
7. Create a scatter plot of:
StudyHours vs PreviousScore

Use different colors for Pass and Fail students.
'''
# Scatter plot of StudyHours vs PreviousScore
plt.figure(figsize=(10, 6))
colors = data['FinalResult'].map({1: 'green', 0: 'red'})
plt.scatter(data['StudyHours'], data['PreviousScore'], c=colors, alpha=0.6)
plt.title('StudyHours vs PreviousScore')
plt.xlabel('StudyHours')
plt.ylabel('PreviousScore')
plt.savefig('study_hours_vs_previous_score.png')  # Save the scatter plot as an image file
plt.show()


'''
8. Draw a boxplot for Attendance.
Identify if any outliers are present.
'''
plt.figure(figsize=(8, 6))
plt.boxplot(data['Attendance'], vert=False)
plt.title('Boxplot of Attendance')
plt.xlabel('Attendance')
plt.savefig('attendance_boxplot.png')  # Save the boxplot as an image file
plt.show()

"""As per the boxplot, there are no significant outliers in the Attendance feature. 
The data appears to be fairly consistent with most values clustered around the median, 
and there are no extreme values that deviate significantly from the rest of the data."""

'''
9. Create a plot showing relationship between AssignmentsCompleted and FinalResult.
Explain your observation.
'''

# Scatter plot of AssignmentsCompleted vs FinalResult
plt.figure(figsize=(10, 6))
colors = data['FinalResult'].map({1: 'blue', 0: 'orange'})
plt.scatter(data['AssignmentsCompleted'], data['FinalResult'], c=colors, alpha=0.6)
plt.title('AssignmentsCompleted vs FinalResult')
plt.xlabel('AssignmentsCompleted')
plt.ylabel('FinalResult')
plt.yticks([0, 1], ['Fail', 'Pass'])
plt.savefig('assignments_completed_vs_final_result.png')  # Save the scatter plot as an image file
plt.show()

"""
Observation:
1. There is a positive relationship between AssignmentsCompleted and FinalResult.
2. Students who completed more assignments are more likely to pass.
3. This suggests that completing assignments is an important factor in determining student success.
"""

'''
10. Plot SleepHours against FinalResult.
Does sleeping more guarantee success? Explain.
'''

# Scatter plot of SleepHours vs FinalResult
plt.figure(figsize=(10, 6))
colors = data['FinalResult'].map({1: 'purple', 0: 'yellow'})
plt.scatter(data['SleepHours'], data['FinalResult'], c=colors, alpha=0.6)
plt.title('SleepHours vs FinalResult')
plt.xlabel('SleepHours')
plt.ylabel('FinalResult')
plt.yticks([0, 1], ['Fail', 'Pass'])
plt.savefig('sleep_hours_vs_final_result.png')  # Save the scatter plot as an image file
plt.show()

"""
Observation:
1. There is no clear relationship between SleepHours and FinalResult.
"""
