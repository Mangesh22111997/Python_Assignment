"""
Question: Write a program which accepts one number and checks whether it is palindrome or not.
Input: 121
Output: Palindrome

"""

def isNumberPalindrom(number):
    numberTravelser = number
    reverseNumber = 0

    while numberTravelser > 0:
        reverseNumber = (reverseNumber * 10) + numberTravelser % 10
        numberTravelser = int(numberTravelser / 10)
        
    return reverseNumber == number
            

def main():
    numberToPass = int(input("Enter number: "))
    if isNumberPalindrom(numberToPass) == True:
        print("Number is Palindrome", )
    else:
        print("Number is not Palindrome", )


if __name__ == "__main__":
    main()