"""
Question: Write a program which accepts two numbers and prints addition, subtraction, multiplication and division.
Input: 12
Output: 1 2 3 4 6 12

"""


def getAdditionOf(number1, number2):
    return number1 + number2

def getSubstractionOf(number1, number2):
    return number1 - number2

def getMultiplicationOf(number1, number2):
    return number1 * number2

def getDivisionOf(number1, number2):
    return number1 / number2

def main():
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

    print("Addition is: ", getAdditionOf(number1, number2)) 
    print("Substraction is: ", getSubstractionOf(number1, number2)) 
    print("Multiplication is: ", getMultiplicationOf(number1, number2)) 
    print("Division is: ", getDivisionOf(number1, number2)) 

if __name__ == "__main__":
    main()