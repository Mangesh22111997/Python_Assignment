"""
Question: Write a program which accepts length and width of rectangle and prints area.

Enter length: 4
Enter Width: 6
Calculated area is:  24

"""

def calculateArea(length, width):
    return length * width

def main():
    length = int(input("Enter length: "))
    width = int(input("Enter Width: "))

    print("Calculated area is: ", calculateArea(length, width))

if __name__ == "__main__":
    main()