"""
Question: Cube of a Number
Write a program which accepts one number and prints the cube of that number.

Example:
Input: 3
Output: 27

"""

def squareNumber(numberToSquare):
    return numberToSquare ** 3

def main():
    print("Enter the number: ")
    number = int(input())

    print("Cube is: ",squareNumber(number) )

if __name__ == "__main__":
    main()