"""
Question: Compare Two Numbers
Write a program which contains one function `ChkGreater()` that accepts two numbers and prints the greater number.

Example:
Input: 10 20
Output: 20 is greater

"""

def checkGreater(firstNumber, secondNumber):
    return firstNumber > secondNumber

def main():
    print("Enter first number: ")
    firstNo = int(input())

    print("Enter second number: ")
    secondNo = int(input())

    if firstNo == secondNo:
        print("Both are equal.")
    elif checkGreater(firstNo, secondNo):
        print(f"{firstNo} is greater")
    else:   
        print(f"{secondNo} is greater")

if __name__ == "__main__":
    main()