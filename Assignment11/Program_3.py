"""
Question: Write a program which accepts one number and prints sum of digits.
Input: 123
Output: 6

"""

def getNumberOfDigitsOf(number):
    numberTravelser = number
    digitCount = 0

    while numberTravelser > 0:
        digitCount = digitCount + int(numberTravelser % 10)
        numberTravelser = int(numberTravelser / 10)
        
    return digitCount
            

def main():
    numberToPass = int(input("Enter number: "))
    print("Number of digits are: ", getNumberOfDigitsOf(numberToPass))

if __name__ == "__main__":
    main()