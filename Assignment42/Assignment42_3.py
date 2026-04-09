"""
3. Use KNN to predict whether a student passes or fails based on study hours and attendance.

Tasks
1. Accept input from user:
◦ Study hours
◦ Attendance percentage
2. Apply KNN algorithm
3. Predict whether the student Passes or Fails

Input Example
Enter Study Hours: 4
Enter Attendance: 70
Expected Output
Predicted Result: Pass
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

#Dataset
data = {"StudyHours": [2, 5, 6, 1],
        "Attendance": [60, 80, 85, 50],
        "FinalResult": ['Fail', 'Pass', 'Pass', 'Fail']}

#Create DataFrame
df = pd.DataFrame(data)
print("Dataset is: \n", df)

def preprocess_data(df):
    df = df.copy()
    df['FinalResult'] = df['FinalResult'].map({'Pass': 1, 'Fail': 0})
    return df

def split_data(df):
    df = preprocess_data(df)
    X = df[['StudyHours', 'Attendance']]
    y = df['FinalResult']
    return train_test_split(X, y, test_size=0.1, random_state=42)

def train_model(X_train, y_train):
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(X_train, y_train)
    return model

def test_model(model, X_test):
    return model.predict(X_test)

def parse_output(prediction):
    return "Pass" if prediction[0] == 0 else "Fail"

def main():
    X_train, X_test, y_train, y_test = split_data(df)
    model = train_model(X_train, y_train)
    y_pred = test_model(model, X_test)
    print("Model Accuracy:", accuracy_score(y_test, y_pred))

    #Inputs
    study_hours = int(input("Enter Study Hours: "))
    attendance = int(input("Enter Attendance: "))
    new_data = pd.DataFrame([[study_hours, attendance]], columns=['StudyHours', 'Attendance'])
    prediction = model.predict(new_data)
    #print("Raw Prediction:", prediction)

    result = parse_output(prediction)
    print("Predicted Result:", result)

if __name__ == "__main__":
    main()
