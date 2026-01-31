"""
Question: Square of a Number
Write a program which accepts one number and prints the square of that number.

Example:
Input: 5
Output: 25

"""

def squareNumber(numberToSquare):
    return numberToSquare ** 2

def main():
    print("Enter the number: ")
    number = int(input())

    print("Square is: ",squareNumber(number) )

if __name__ == "__main__":
    main()