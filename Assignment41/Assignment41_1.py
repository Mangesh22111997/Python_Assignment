"""
1. Write a Python program that classifies a new data point using the K-Nearest Neighbors algorithm.
The algorithm should be implemented manually without using any machine learning library.
The program should:
• Calculate Euclidean distance
• Sort distances
• Select K nearest neighbors
• Predict the class based on majority voting

Tasks
1. Accept X and Y coordinates of a new point from the user.
2. Compute Euclidean distance from all dataset points.
3. Sort the distances.
4. Select K = 3 nearest neighbors.
5. Predict the class label.

Input Format
Enter X coordinate: 2
Enter Y coordinate: 2
Expected Output
Nearest Neighbors:
A - Distance: 1.0
B - Distance: 1.0
C - Distance: 1.41
Predicted Class: Red
"""

import pandas as pd
import numpy as np

data = {"Point": ['A', 'B', 'C', 'D'],
        "X": [1,2,3,6],
        "Y": [2,3,1,5],
        "Label": ['Red', 'Red', 'Blue', 'Blue']}

#Create DataFrame
df = pd.DataFrame(data)

print("Dataset is: \n", df)

#Calculate Euclidean distance
#Step 5
def euclidean_distance(point1, point2):
    point1_x1, point1_y1 = point1
    point2_x2, point2_y2 = point2
    return np.sqrt((point2_x2-point1_x1)**2 + (point2_y2-point1_y1)**2)

#Sort distances
#Step 4
def calculate_distances(df, new_point):
    distances = []
    for index, row in df.iterrows():
        existing_point = (row['X'], row['Y'])
        distance = euclidean_distance(existing_point, new_point)
        distances.append((distance, row['Point'], row['Label']))

    print(distances)
    return distances

#Step 3
def sort_distances(df, new_point):
    distances = calculate_distances(df, new_point)
    distances.sort(key=lambda x: x[0])
    return distances

#Select K nearest neighbors
#Step 2
def k_nearest_neighbors(df, new_point, k):
    sorted_distances = sort_distances(df, new_point)
    neighbors = sorted_distances[:k]
    print("Nearest Neighbors:")
    for distance, point, label in neighbors:
        print(f"{point} - Distance: {distance:.2f}")
    return neighbors

#Predict the class based on majority voting
#Step 1
def predict_class(df, new_point, k):
    neighbors = k_nearest_neighbors(df, new_point, k)
    labels = [neighbor[2] for neighbor in neighbors]
    predicted_label = max(set(labels), key=labels.count)
    return predicted_label

#updating the df with calculated distances for better visualization
def update_df_with_distances(df, new_point):
    distances = calculate_distances(df, new_point)
    df['Distance'] = [distance[0] for distance in distances]
    return df

#print("Dataset with calculated distances: \n", update_df_with_distances(df, (4, 4)))
def main():
    input_x = int(input("Enter X coordinate: "))
    input_y = int(input("Enter Y coordinate: "))
    new_point = (input_x, input_y)
    k = 5
    predicted_label = predict_class(df, new_point,k )
    print(f"Predicted Class: {predicted_label}")

if __name__ == "__main__":
    main()
