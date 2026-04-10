"""
3. Consider below task
1. Train linear regression model.
2. Predict salary for 6 years of experience.
3. Plot regression line using matplotlib.

Expected Output
Predicted Salary for 6 Years Experience: ₹45000
Graph should display:
• Data points
• Regression line
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def train_linear_regression(X, Y):
    model = LinearRegression()
    model.fit(X.reshape(-1, 1), Y)
    return model

def main():
    # Sample data (replace with actual dataset)
    X = np.array([1, 2, 3, 4, 5])
    Y = np.array([20000, 25000, 30000, 35000, 40000])

    # Train the model
    model = train_linear_regression(X, Y)

    # Predict salary for 6 years of experience
    predicted_salary = model.predict(np.array([[6]]))
    print(f"Predicted Salary for 6 Years Experience: ₹{int(predicted_salary[0])}")

    # Plot the regression line
    plt.scatter(X, Y, color='blue', label='Data points')
    plt.plot(X, model.predict(X.reshape(-1, 1)), color='red', label='Regression line')
    plt.xlabel('Years of Experience')
    plt.ylabel('Salary')
    plt.title('Linear Regression: Salary vs Years of Experience')
    plt.legend()
    plt.savefig("salary_regression.png")
    plt.show()
    plt.close()

if __name__ == "__main__":
    main()