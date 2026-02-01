"""
Question: Write a program which accepts one number and prints binary equivalent.
Enter Number: 2
Output: 0b10

"""
from math import pi

def binaryOfNumber(number):
    print(bin(number))

def main():
    number = int(input("Enter Number: "))
    binaryOfNumber(number)


if __name__ == "__main__":
    main()