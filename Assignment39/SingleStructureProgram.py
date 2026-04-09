"""
8. Write a single structured Python program that performs:
1. Dataset loading
2. Data analysis
3. Visualization
4. Train-test split
5. Model training
6. Prediction
7. Accuracy calculation
8. Confusion matrix generation
9. Final conclusion
Your code should include proper comments explaining each step.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split        
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay

def load_data(file_path):
    return pd.read_csv(file_path)

def analyze_data(data):
    print(data.head())
    print(data.tail())
    print("Shape of the dataset:", data.shape)
    print("Data types of each column:\n", data.dtypes)
    print(data.describe())
    print("Columns in the dataset:", data.columns)
    print("Missing values in each column:\n", data.isnull().sum())
    print("Distribution of Target:\n", data['FinalResult'].value_counts())

def visualize_data(data):
    data['FinalResult'].value_counts().plot(kind='bar')
    plt.title('Distribution of Final Result')
    plt.xlabel('Final Result (0=Fail, 1=Pass)')
    plt.ylabel('Count')
    plt.grid(axis='y')
    plt.savefig("final_result_distribution.png")
    plt.show()

    data.boxplot(column=['StudyHours', 'Attendance', 'PreviousScore', 'AssignmentsCompleted', 'SleepHours'],
                  by='FinalResult')
    plt.show()
    
    data.plot.scatter(x='StudyHours', y='PreviousScore', c='FinalResult', cmap='viridis')
    plt.title('Study Hours vs Previous Score')
    plt.savefig("study_hours_vs_previous_score.png")
    plt.show()   

def train_model(X_train, y_train):
    model = DecisionTreeClassifier(max_depth=None, random_state=42)
    model.fit(X_train, y_train)
    return model

def prediction(model, X_test):
    return model.predict(X_test)

def calculate_accuracy(y_test, y_pred):
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {round(accuracy * 100, 2)}%")
    return accuracy

def generate_confusion_matrix(y_test, y_pred, model):
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
    disp.plot(cmap=plt.cm.Blues)
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted Label")
    plt.ylabel("True Label")
    plt.grid(False)
    plt.savefig("confusion_matrix.png")
    plt.show()




def main():
    data = load_data("student_performance_ml.csv")
    analyze_data(data)
    visualize_data(data)

    X = data.drop("FinalResult", axis=1)
    y = data["FinalResult"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = train_model(X_train, y_train)
    y_pred = prediction(model, X_test)

    calculate_accuracy(y_test, y_pred)
    generate_confusion_matrix(y_test, y_pred, model)

if __name__ == "__main__":
    main()

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              