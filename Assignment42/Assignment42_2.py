'''
2. Using the same dataset from above question, calculate model performance.
Tasks
1. Predict all Y values using regression equation.
2. Calculate:
• Mean Squared Error (MSE)
• R2 Score
Show all intermediate calculations.
'''

import pandas as pd
import numpy as np

def mean_x(X):
    return np.mean(X)

def mean_y(Y):
    return np.mean(Y)

def slope(X, Y):
    X_mean = mean_x(X)
    Y_mean = mean_y(Y)
    numerator = np.sum((X - X_mean) * (Y - Y_mean))
    denominator = np.sum((X - X_mean) ** 2)
    return numerator / denominator

def intercept(X, Y, m):
    X_mean = mean_x(X)
    Y_mean = mean_y(Y)
    return Y_mean - m * X_mean

def predict(m, c, X):
    return m * X + c

def main():
    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]

    X_mean = mean_x(X)
    Y_mean = mean_y(Y)
    m = slope(X, Y)
    c = intercept(X, Y, m)

    print(f"Mean of X = {X_mean}")
    print(f"Mean of Y = {Y_mean}")
    print(f"Slope (m) = {m}")
    print(f"Intercept (c) = {c}")
    print(f"Regression Equation:\nY = {m}X + {c}")

    predicted_Y = [predict(m, c, x) for x in X]
    print(f"Predicted Y values: {predicted_Y}")

    mse = np.mean((np.array(Y) - np.array(predicted_Y)) ** 2)
    r2_score = 1 - (np.sum((np.array(Y) - np.array(predicted_Y)) ** 2) / np.sum((np.array(Y) - Y_mean) ** 2))

    print(f"Mean Squared Error (MSE): {mse}")
    print(f"R2 Score: {round(r2_score, 2)}")

if __name__ == "__main__":
    main()