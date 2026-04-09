"""
1. After training the Decision Tree model, use:
model.feature_importances_
• Display importance score of each feature.
• Which feature contributes the most in predicting FinalResult?
• Which feature contributes the least?

2. Remove the column SleepHours from the dataset.
• Train the model again.
• Compare new accuracy with previous accuracy.
• Does removing this feature affect performance?

3. Train the model using only:
• StudyHours
• Attendance
Compare the accuracy with the full-feature model.
Is the model still performing well?

4. Create a new DataFrame with details of 5 new students.
Use the trained model to predict their results.
Display predictions clearly.

5. Without using accuracy_score, manually calculate accuracy:
Verify whether it matches sklearn accuracy.

6. Identify students where:
y_test != y_pred
• Display those rows.
• How many students were misclassified?
• What common pattern do you observe?

7. Train model using:
• random_state = 0
• random_state = 10
• random_state = 42
Compare testing accuracy.
Does the result change?

8. Decision Tree Visualization
Use:
from sklearn.tree import plot_tree
Visualize the trained decision tree.
• Which feature appears at the root node?
• Why do you think that feature was selected first?

9. Create a new column:
PerformanceIndex = (StudyHours * 2) + Attendance
Train the model including this new feature.
Does accuracy improve?

10. Train model with:
• max_depth = None
Calculate:
• Training accuracy
• Testing accuracy
If training accuracy is 100% but testing accuracy is lower, explain why this happens.

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

Border = "*" * 50

print(Border)
#3. Calculate model accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {round(accuracy * 100, 2)}%")

#feature importance
feature_importance = model.feature_importances_
feature_names = X.columns
importance_df = pd.DataFrame({"Feature": feature_names, "Importance": feature_importance})
print(importance_df.sort_values(by="Importance", ascending=False))

print(Border)
"""
Attendance contributes the most in predicting FinalResult, while SleepHours contributes the least.
"""

print(Border)
#Remove SleepHours and retrain the model
X_new = X.drop("SleepHours", axis=1)
X_train_new, X_test_new, y_train_new, y_test_new = train_test_split(X_new, y, test_size=0.2, random_state=42)
model_new = DecisionTreeClassifier(max_depth=None, random_state=42)
model_new.fit(X_train_new, y_train_new)
y_pred_new = model_new.predict(X_test_new)
accuracy_new = accuracy_score(y_test_new, y_pred_new)
print(f"New Model Accuracy without SleepHours: {round(accuracy_new * 100, 2)}%")

feature_importance_new = model_new.feature_importances_
feature_names_new = X_new.columns
importance_df_new = pd.DataFrame({"Feature": feature_names_new, "Importance": feature_importance_new})
print(importance_df_new.sort_values(by="Importance", ascending=False))

print(Border)

''' Removing SleepHours does not reduce the accuracy, indicating it is not a critical feature. 
Attendance remains the most important feature even after removing SleepHours.'''


#Train model using only StudyHours and Attendance
print(Border)

X_reduced = X[["StudyHours", "Attendance"]]
X_train_reduced, X_test_reduced, y_train_reduced, y_test_reduced = train_test_split(X_reduced, y, test_size=0.2, random_state=42)
model_reduced = DecisionTreeClassifier(max_depth=None, random_state=42)
model_reduced.fit(X_train_reduced, y_train_reduced)
y_pred_reduced = model_reduced.predict(X_test_reduced)
accuracy_reduced = accuracy_score(y_test_reduced, y_pred_reduced)
print(f"Model Accuracy with only StudyHours and Attendance: {round(accuracy_reduced * 100, 2)}%")

feature_importance_reduced = model_reduced.feature_importances_
feature_names_reduced = X_reduced.columns
importance_df_reduced = pd.DataFrame({"Feature": feature_names_reduced, "Importance": feature_importance_reduced})
print(importance_df_reduced.sort_values(by="Importance", ascending=False))


''' The model still performs well with only StudyHours and Attendance, 
indicating these features are strong predictors of FinalResult.'''
print(Border)

# Create new DataFrame with details of 5 new students
new_students = pd.DataFrame({
    "StudyHours": [5, 2, 8, 1, 4],
    "Attendance": [90, 60, 95, 50, 80],
    "PreviousScore": [85, 70, 90, 60, 75],
    "AssignmentsCompleted": [10, 5, 12, 3, 8],
    "SleepHours": [7, 6, 8, 5, 6]
})

new_students_predictions = model.predict(new_students)

new_students["PredictedFinalResultusingAllFeatures"] = new_students_predictions
print(new_students)

print(Border)

# Manually calculate accuracy

def accuracy_manual(y_true, y_pred):
    correct_predictions = sum(y_true == y_pred)
    total_predictions = len(y_true)
    accuracy = correct_predictions / total_predictions
    return accuracy

manual_accuracy = accuracy_manual(y_test, y_pred)
print(f"Manually Calculated Accuracy: {round(manual_accuracy * 100, 2)}%")

#Full featured model accuracy comparison
manual_accuracy_full = accuracy_manual(y_test, y_pred)
print(f"Full-feature model accuracy: {round(manual_accuracy_full * 100, 2)}%")
print(f"sklearn model accuracy: {round(accuracy * 100, 2)}%")

#SleepHours removed model accuracy comparison
manual_accuracy_no_sleep = accuracy_manual(y_test_new, y_pred_new)
print(f"Model accuracy without SleepHours: {round(manual_accuracy_no_sleep * 100, 2)}%")
print(f"sklearn model accuracy without SleepHours: {round(accuracy_new * 100, 2)}%")

#Reduced feature model accuracy comparison
manual_accuracy_reduced = accuracy_manual(y_test_reduced, y_pred_reduced)
print(f"Reduced-feature model accuracy: {round(manual_accuracy_reduced * 100, 2)}%")
print(f"sklearn model accuracy with reduced features: {round(accuracy_reduced * 100, 2)}%")


'''
The manually calculated accuracy matches the sklearn accuracy, confirming that our manual calculation is correct.
'''
print(Border)

#Identify misclassified students

misclassified_students = results[results["Actual"] != results["Predicted"]]
print("Misclassified Students:\n", misclassified_students)

'''
There is no misclassification in this model, indicating that all predictions are correct.
'''
print(Border)

# Train model with different random states and compare accuracy
random_states = [0, 10, 42]

#all features model
for state in random_states:
    model_random = DecisionTreeClassifier(max_depth=None, random_state=state)
    model_random.fit(X_train, y_train)
    y_pred_random = model_random.predict(X_test)
    accuracy_random = accuracy_score(y_test, y_pred_random)
    print(f"Model Accuracy with random_state={state}: {round(accuracy_random * 100, 2)}%")

'''
Accuracy remains consistent across different random states, indicating that the model's performance is stable 
and not sensitive to the choice of random state.
'''

print(Border)

#Visualize the decision tree

from sklearn.tree import plot_tree

plot_trees = {
    "full_features": model, 
    "no_sleep_feature": model_new, 
    "reduced_featured": model_reduced
}

for title, tree_model in plot_trees.items():
    # Create a fresh figure for every tree to avoid overlapping
    plt.figure(figsize=(15, 10)) 
    current_features = tree_model.feature_names_in_
    print("Current features for model:", title)
    print("Feature names:", current_features)
    # Identify the correct feature names for each specific model
    # Note: If models have different features, you may need a mapping for X.columns
    plot_tree(
        tree_model, 
        feature_names=current_features, 
        class_names=[str(c) for c in tree_model.classes_], 
        filled=True,
        fontsize=10
    )
    
    plt.title(f"Decision Tree Visualization - {title}")
    plt.savefig(f"decision_tree_{title}.png", bbox_inches='tight')
    plt.show()
    plt.close() 

print(Border)

#Create a new column PerformanceIndex and retrain the model

print("Original Data: \n", data.head())

new_data = data.copy()

#Add new column
new_data["PerformanceIndex"] = (new_data["StudyHours"] * 2) + new_data["Attendance"]
print("Data with PerformanceIndex: \n", new_data.head())

#Prepare new features and target variable
X_new_index = new_data.drop("FinalResult", axis=1)
y_new_index = new_data["FinalResult"]

#Split the dataset
X_train_index, X_test_index, y_train_index, y_test_index = train_test_split(X_new_index, y_new_index, test_size=0.2, random_state=42)

#Train the model with new feature
model_index = DecisionTreeClassifier(max_depth=None, random_state=42)
model_index.fit(X_train_index, y_train_index)
y_pred_index = model_index.predict(X_test_index)
accuracy_index = accuracy_score(y_test_index, y_pred_index)
print(f"Model Accuracy with PerformanceIndex: {round(accuracy_index * 100, 2)}%")

feature_importance_index = model_index.feature_importances_
feature_names_index = X_new_index.columns
importance_df_index = pd.DataFrame({"Feature": feature_names_index, "Importance": feature_importance_index})
print(importance_df_index.sort_values(by="Importance", ascending=False))

print(Border)

''' The model accuracy may improve slightly with the addition of PerformanceIndex,
indicating that this new feature captures additional information that helps in predicting FinalResult.
However, the improvement may not be significant if the original features already capture most of the variance 
in the target variable.'''

#train the model with max_depth = None and compare training and testing accuracy

model_max_depth = DecisionTreeClassifier(max_depth=None, random_state=42)
model_max_depth.fit(X_train_index, y_train_index)
y_pred_max_depth = model_max_depth.predict(X_test_index)
accuracy_max_depth = accuracy_score(y_test_index, y_pred_max_depth)
print(f"Model Accuracy with max_depth=None: {round(accuracy_max_depth * 100, 2)}%")

training_accuracy_max_depth = accuracy_score(y_train_index, model_max_depth.predict(X_train_index))
print(f"Training Accuracy with max_depth=None: {round(training_accuracy_max_depth * 100, 2)}%")

testing_accuracy_max_depth = accuracy_score(y_test_index, y_pred_max_depth)
print(f"Testing Accuracy with max_depth=None: {round(testing_accuracy_max_depth * 100, 2)}%")

"""
Not much difference in training and testing accuracy with max_depth=None, indicating that the model is not overfitting.
If training accuracy was 100% but testing accuracy was significantly lower, it would indicate that the
model is overfitting the training data and not generalizing well to unseen data.
"""

