'''
2. The value of K plays an important role in the KNN algorithm.
Write a Python program that demonstrates how prediction changes when K changes.
Dataset
Use the same dataset as Assignment 1.
Tasks
Predict the class of the same new point using:
• K = 1
• K = 3
• K = 5
Expected Output
Prediction Results
K = 1 → Red
K = 3 → Red
K = 5 → Blue
Explain why the prediction changes when K increases.
'''
from Assignment41_1 import df, euclidean_distance, calculate_distances, sort_distances

def main():
    input_x = int(input("Enter X coordinate: "))
    input_y = int(input("Enter Y coordinate: "))
    new_point = (input_x, input_y)

    sorted_distances = sort_distances(df, new_point)
    print("Sorted Distances:")

    for distance, point, label in sorted_distances:
        print(f"{point} - Distance: {distance:.2f}")

    print("_" * 50)

    for k in [1, 3, 5, 10]:
        neighbors = sorted_distances[:k]
        labels = [neighbor[2] for neighbor in neighbors]
        predicted_label = max(set(labels), key=labels.count)
        print(f"K = {k} → Predicted Label: {predicted_label}")

"""
The Value of K in KNN determines how many nearest neighbors are considered when making a prediction.
When K is small (e.g., K=1), the prediction is based on the closest neighbor, which can lead to a 
more flexible model that may capture noise in the data. 
As K increases, the model becomes more generalized, as it considers more neighbors for making a 
prediction. This can lead to a smoother decision boundary and may help reduce the impact of outliers.
However, if K is too large, it may include neighbors that are not relevant to the new point, leading
to incorrect predictions. Therefore, 
choosing an appropriate value of K is crucial for the performance of the KNN algorithm.  

Hence, when the k value is increased, the prediction may change because the algorithm is considering
more neighbors, which can lead to a different majority class among those neighbors. 
This is why the prediction can change as K increases.

"""

if __name__ == "__main__":
    main()