"""
Question: Write a program which accepts one number and prints reverse of that number.
Input: 123
Output: 321

"""

def getReverseOfNumber(number):
    numberTravelser = number
    reverseNumber = 0

    while numberTravelser > 0:
        reverseNumber = (digitCount * 10) + numberTravelser % 10
        numberTravelser = int(numberTravelser / 10)
        
    return reverseNumber
            

def main():
    numberToPass = int(input("Enter number: "))
    print("Number of digits are: ", getReverseOfNumber(numberToPass))

if __name__ == "__main__":
    main()