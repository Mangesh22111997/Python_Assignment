"""
1. Implement Simple Linear Regression manually without using any ML library.
Dataset
X = [1,2,3,4,5]
Y = [3,4,2,4,5]

Tasks
Calculate:
1. Mean of X (X̄ )
2. Mean of Y (Ȳ)
3. Slope (m)
4. Intercept (c)

Expected Output Example
Mean of X = 3
Mean of Y = 3.6
Slope (m) = 0.4
Intercept (c) = 2.4
Regression Equation:
Y = 0.4X + 2.4
Predicted Y for X = 6 : 4.8
"""
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
    print(f"Predicted Y for X = 6 : {round(predict(m, c, 6), 1)}")


if __name__ == "__main__":
    main()