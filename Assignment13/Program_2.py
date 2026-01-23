"""
Question: Write a program which accepts radius of circle and prints area of circle.

Enter Radius: 4
Calculated area is:  25.132741228718345

"""
from math import pi

def calculateAreaOfCircleFrom(radius):
    return 2*pi*radius

def main():
    radius = int(input("Enter Radius: "))
    print("Calculated area is: ", calculateAreaOfCircleFrom(radius))

if __name__ == "__main__":
    main()