"""
There is one data set of wether conditions.
That dataset contains information as wether and we have to decides whether to play or
not.
Data set contains the target variable as Play which indicates whether to play or not.
Consider below Marvellous Infosystems Play Predictor Dataset as:

According to above dataset there are two features as
1.Weather
2.Temperature

We have two labels as
1.Yes
2.No

There are three types of different entries under Wether as
1.Sunny
2.Overcast
3.Rainy

There are three types of different entries under Temperature as
1.Hot
2.Cold
3.Mild

We have to design Machine Learning application which uses Classification
technique.
###############################################################################
Design machine learning application which follows below steps as

Step 1:
Get Data
Load data from MarvellousInfosystems_PlayPredictor.csv file into python application.

Step 2:
Clean, Prepare and Manipulate data
As we want to use the above data into machine learning application we have prepare
that in the format which is accepted by the algorithms.
As our dataset contains two features as Wether and Temperature. We have to replace
each string field into numeric constants by using LabelEncoder from processing module
of sklearn.

Step 3:
Train Data
Now we want to train our data for that we have to select the Machine learning algorithm.
For that we select K Nearest Neighbour algorithm.
use fit method for training purpose. For training use whole dataset.

Step 4:
Test Data
After successful training now we can test our trained data by passing some value of
wether and temperature.
As we are using KNN algorithm use value of K as 3.
After providing the values check the result and display on screen.
Result may be Yes or No.

Step 5:
Calculate Accuracy
Write one function as CheckAccuracy() which calculate the accuracy of our algorithm.
For calculating the accuracy divide the dataset into two equal parts as Training data and
Testing data.
Calculate Accuracy by changing value of K.
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay


#Load Data
def load_data(file_path):
    return pd.read_csv(file_path)

#Prepare Data
def preprocess_data(df):
    print("Shape of Dataset: ", df.shape)
    print("Columns in Dataset: ", df.columns)
    print("No. of columns in Dataset: ", len(df.columns))
    print("No of data entries in dataset: ", len(df))
    print("Data types of each column:\n", df.dtypes)
    print("Missing values in each column:\n", df.isnull().sum())
    print("Unique values in each column:\n", df.nunique())

    #use label encoder for converting string data into numeric constants
    label_encoder = LabelEncoder()
    df['Weather'] = label_encoder.fit_transform(df['Weather'])
    df['Temperature'] = label_encoder.fit_transform(df['Temperature'])
    df['Play'] = label_encoder.fit_transform(df['Play'])
    return df

#Drop column
def drop_column(df, column_name):
    return df.drop(column_name, axis=1)

#Split data into training and testing data
def split_data(df, column_name):
    X = df.drop(column_name, axis=1)
    y = df[column_name]
    return train_test_split(X, y, test_size=0.2, random_state=42)

#Train Data
def train_model(X_train, y_train):
    knn_model = KNeighborsClassifier(n_neighbors=3)
    knn_model.fit(X_train, y_train)
    return knn_model

#Test Data
def test_model(model, X_test):
    return model.predict(X_test)

#Convert predictions to original labels
def convert_predictions(predictions):
    label_encoder = LabelEncoder()
    label_encoder.fit(['No', 'Yes'])
    return label_encoder.inverse_transform(predictions)

#Calculate Accuracy
def check_accuracy(y_test, y_pred):
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: ", round(accuracy, 2)*100, "%")
    print("Classification Report:\n", classification_report(y_test, y_pred))
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot()

def main():
    file_path = "PlayPredictor.csv"

    #load data
    df = load_data(file_path)
    print("Original Data:\n", df.head())

    #Analyze and preprocess data
    df = preprocess_data(df)
    print("Preprocessed Data:\n", df.head())

    #Drop column
    df = drop_column(df, 'Unnamed: 0')
    print("Data after dropping column:\n", df.head())

    #Split data into training and testing data
    X_train, X_test, y_train, y_test = split_data(df, 'Play')
    print("Training Data Shape: ", X_train.shape)
    print("Testing Data Shape: ", X_test.shape)

    #Train model
    model = train_model(X_train, y_train)

    #Test model
    y_pred = test_model(model, X_test)
    y_pred_converted = convert_predictions(y_pred)
    print("Predicted Values: ", y_pred_converted)

    #Calculate accuracy
    check_accuracy(y_test, y_pred)


if __name__ == "__main__":
    main()
    