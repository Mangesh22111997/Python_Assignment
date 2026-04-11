"""
There is one data set of wine which classify the wines according to its contents into three
classes.
Consider below Wine Dataset as:

These data are the results of a chemical analysis of wines grown in the same region in Italy
but derived from three different cultivars. The analysis determined the quantities of 13
constituents found in each of the three types of wines.

Wine data set contains 13 features as
1) Alcohol
2) Malic acid
3) Ash
4) Alcalinity of ash
5) Magnesium
6) Total phenols
7) Flavanoids
8) Nonflavanoid phenols
9) Proanthocyanins
10)Color intensity
11)Hue
12)OD280/OD315 of diluted wines
13)Proline

According to the above features wine can be classified as
• Class 1
• Class 2
• Class 3

Design machine learning application which follows below steps as

Step 1:
Get Data

Step 2:
Clean, Prepare and Manipulate data

Step 3:
Train Data

Step 4:
Test Data

Step 5:
Calculate Accuracy

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay

#save models
import joblib
import pickle


#Read dataset
def load_data(file_path):
    return pd.read_csv(file_path)

#Drop unnecessary columns
def drop_columns(df):
    return df.drop(columns=['Unnamed: 0'])

#Analyze data
def analyze_data(data):
    print(data.head())
    print(data.tail())
    print("Shape of the dataset:", data.shape)
    print("Data types of each column:\n", data.dtypes)
    print(data.describe())
    print("Columns in the dataset:", data.columns)
    print("Missing values in each column:\n", data.isnull().sum())
    print("Distribution of Target Column:\n", data['Class'].value_counts())
    print("Correlation between features:\n", data.corr())

#Split data into training and testing sets
def split_data(data):
    X = data.drop(columns=['Class'])
    y = data['Class']
    return train_test_split(X, y, test_size=0.3, random_state=42)

#Train model
def train_model(X_train, y_train, model_name):
    model = model_name
    
    model.fit(X_train, y_train)
    return model

#Test model
def test_model(model, X_test):
    return model.predict(X_test)

#Calculate accuracy``
def calculate_accuracy(y_test, y_pred):
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: ", round(accuracy * 100, 2), "%")

#Display predicted and expected values
def display_results(y_test, y_pred):
    results_df = pd.DataFrame({'Expected': y_test, 'Predicted': y_pred})
    print(results_df)

def save_model_pickle(model, file_name):
    with open(file_name, 'wb') as file:
        pickle.dump(model, file)

def save_model_joblib(model, file_name):
    joblib.dump(model, file_name)

def main():
    #load data
    data = load_data("WinePredictor.csv")

    #Analyze data
    analyze_data(data)

    #Split data into training and testing sets
    X_train, X_test, y_train, y_test = split_data(data)

    #models to train
    models = {
        "Decision Tree": DecisionTreeClassifier(max_depth=None, random_state=42),
        "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
        "K-Nearest Neighbors": KNeighborsClassifier(n_neighbors=3),
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42)
    }

    #Train multiple models
    model_dt = train_model(X_train, y_train, models["Decision Tree"])
    model_lr = train_model(X_train, y_train, models["Logistic Regression"])
    model_knn = train_model(X_train, y_train, models["K-Nearest Neighbors"])
    model_rf = train_model(X_train, y_train, models["Random Forest"])

    #Test multiple models
    y_pred_dt = test_model(model_dt, X_test)
    y_pred_lr = test_model(model_lr, X_test)
    y_pred_knn = test_model(model_knn, X_test)
    y_pred_rf = test_model(model_rf, X_test)

    #Calculate accuracy for each model
    print("Decision Tree Accuracy:")
    calculate_accuracy(y_test, y_pred_dt)

    print("Logistic Regression Accuracy:")
    calculate_accuracy(y_test, y_pred_lr)

    print("K-Nearest Neighbors Accuracy:")
    calculate_accuracy(y_test, y_pred_knn)

    print("Random Forest Accuracy:")
    calculate_accuracy(y_test, y_pred_rf)

    #Save models using pickle
    save_model_pickle(model_dt, "decision_tree_model.pkl")
    save_model_pickle(model_lr, "logistic_regression_model.pkl")
    save_model_pickle(model_knn, "knn_model.pkl")
    save_model_pickle(model_rf, "random_forest_model.pkl")

    #Save models using joblib
    save_model_joblib(model_dt, "decision_tree_model.joblib")
    save_model_joblib(model_lr, "logistic_regression_model.joblib")
    save_model_joblib(model_knn, "knn_model.joblib")
    save_model_joblib(model_rf, "random_forest_model.joblib")

    #Display predicted and expected values for all models
    print("Decision Tree Results:")
    display_results(y_test, y_pred_dt)

    print("Logistic Regression Results:")
    display_results(y_test, y_pred_lr)

    print("K-Nearest Neighbors Results:")
    display_results(y_test, y_pred_knn)

    print("Random Forest Results:")
    display_results(y_test, y_pred_rf)


if __name__ == "__main__":
    main()