"""
Question: Write a program which accepts one number and prints count of digits in that number.
Input: 7521
Output: 4

"""

def getNumberOfDigitsOf(number):
    numberTravelser = number
    digitCount = 0

    while numberTravelser > 0:
        numberTravelser = int(numberTravelser / 10)
        digitCount += 1
        
    return digitCount
            

def main():
    numberToPass = int(input("Enter number: "))
    print("Number of digits are: ", getNumberOfDigitsOf(numberToPass))

if __name__ == "__main__":
    main()