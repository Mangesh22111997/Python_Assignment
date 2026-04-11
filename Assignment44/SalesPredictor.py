"""
There is one data set of advertisement agency.
Consider below Dataset as:

Dataset contains multiple records about the customers who invest in multiple advertisement
options.
Depends on that sales feature indicates the the increased amount in there sales
This data set contains 4 features as
TV
Radio
Television
Depends on the above three features Sales feature indicates the increased sale amount.

We have to design Machine Learning application which uses Classification
technique.

Design machine learning application which follows below steps as

Step 1:
Get Data
Load data from MarvellousAdvertising.csv file into python application.

Step 2:
Clean, Prepare and Manipulate data
As we want to use the above data into machine learning application we have prepare
that in the format which is accepted by the algorithms.

Step 3:
Train Data
Now we want to train our data for that we have to select the Machine learning algorithm.
For that we select Linear Regression algorithm from sykit learn library.
For training purpose divide the dataset into half part.
Use train method to train our dataset.

Step 4:
Test the data
Test data by passing the remaining half part of the data set.

Step 5:
Display predicted values of Linear regression algorithms as well as expected values
which are provided by the data set.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

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
    print("Distribution of Sales:\n", data['sales'].value_counts())
    print("Correlation between features:\n", data.corr())

#Split data into training and testing sets
def split_data(data):
    X = data.drop(columns=['sales'])
    y = data['sales']
    return train_test_split(X, y, test_size=0.3, random_state=42)

#Train model
def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

#Test model
def test_model(model, X_test):
    return model.predict(X_test)

#Calculate accuracy
def calculate_accuracy(y_test, y_pred):
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print("Mean Squared Error: ", mse)
    print("R^2 Score: ", round(r2 * 100, 2), "%")

#Display predicted and expected values
def display_results(y_test, y_pred):
    results_df = pd.DataFrame({'Expected': y_test, 'Predicted': y_pred})
    print(results_df)

def main():
    #laod data
    data = load_data("Advertising.csv")
    #Drop unnecessary columns
    data = drop_columns(data)

    #Analyze data
    analyze_data(data)

    #Split data into training and testing sets
    X_train, X_test, y_train, y_test = split_data(data)

    #Train model
    model = train_model(X_train, y_train)

    #Test model
    y_pred = test_model(model, X_test)
    y_pred = np.round(y_pred, 2)  # Round predictions to 2 decimal points

    #Calculate accuracy
    calculate_accuracy(y_test, y_pred)

    #Display predicted and expected values
    display_results(y_test, y_pred)

if __name__ == "__main__":
    main()