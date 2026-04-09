"""
1. Import DecisionTreeClassifier from sklearn.
Create a model object and train it using fit().

2. Use the trained model to predict results for X_test.
Display predicted values along with actual values.

3. Calculate model accuracy using accuracy_score.
Display the result in percentage format.

4. Generate confusion matrix using sklearn.
Display it using ConfusionMatrixDisplay.
Explain clearly:
• True Positive
• True Negative
• False Positive
• False Negative

5. Calculate:
• Training accuracy
• Testing accuracy
Compare both and comment whether the model is overfitting or underfitting.

6. Train three Decision Tree models with:
• max_depth = 1
• max_depth = 3
• max_depth = None
Compare their testing accuracies and write your observations.

7. Use the trained model to predict result for a student with:
• StudyHours = 6
• Attendance = 85
• PreviousScore = 66
• AssignmentsCompleted = 7
• SleepHours = 7
Will the student Pass or Fail?


"""

#Importing necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

#Load the dataset
data = pd.read_csv("student_performance_ml.csv")

#Data preprocessing
X = data.drop("FinalResult", axis=1)  # Features
y = data["FinalResult"]  # Target variable

#Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#1. Train the Decision Tree model
model = DecisionTreeClassifier(max_depth=None, random_state=42)

model.fit(X_train, y_train)

#2. Predict results for X_test
y_pred = model.predict(X_test)

#Display predicted values along with actual values
results = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})
print(results)

#3. Calculate model accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {round(accuracy * 100, 2)}%")

#4. Generate confusion matrix
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
disp.plot(cmap=plt.cm.Blues)
plt.title("Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.grid(False)
plt.savefig("confusion_matrix.png")  # Save the confusion matrix as an image
plt.show()

#5. Calculate training and testing accuracy
train_accuracy = accuracy_score(y_train, model.predict(X_train))
test_accuracy = accuracy_score(y_test, y_pred)
print(f"Training Accuracy: {round(train_accuracy * 100, 2)}%")
print(f"Testing Accuracy: {round(test_accuracy * 100, 2)}%")

#6. Train three Decision Tree models with different max_depth
depths = [1, 3, None]

for depth in depths:
    model = DecisionTreeClassifier(max_depth=depth, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Training Accuracy with max_depth={depth}: {round(accuracy_score(y_train, model.predict(X_train)) * 100, 2)}%")
    print(f"Testing Accuracy with max_depth={depth}: {round(accuracy * 100, 2)}%")



#7. Predict result for a new student
new_student = [[6, 85, 66,7,7]]  # StudyHours, Attendance, PreviousScore, AssignmentsCompleted, SleepHours
predicted_result = model.predict(new_student)
if predicted_result[0] == 1:
    print("The student is predicted to Pass.")
else:
    print("The student is predicted to Fail.")



