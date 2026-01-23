"""
Question: Divisibility Check
Write a program which accepts one number and checks whether it is divisible by both 3 and 5.

Example:

Input: 15
Output: Divisible by 3 and 5

"""

def isDivisibleByThreeAndFive(numberToCheck):
    return (numberToCheck % 3 == 0) and (numberToCheck % 5 == 0)

def main():
    print("Enter the number: ")
    number = int(input())

    if isDivisibleByThreeAndFive(number):
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")

if __name__ == "__main__":
    main()