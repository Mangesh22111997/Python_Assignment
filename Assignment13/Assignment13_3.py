"""
Question: Write a program which accepts one number and checks whether it is perfect number or not.

Input: 6
Output: Perfect Number

Hint: - a positive integer that is equal to the sum of its positive proper divisors.
      - 6 and 28 is a perfect number

"""
from math import pi

def isPerfectNumber(number):
    sumOfDivisibles = 0
    for i in range(1, number):
        if number % i == 0:
            sumOfDivisibles = sumOfDivisibles + i
   
    return sumOfDivisibles == number

def main():
    number = int(input("Enter Number: "))

    if number < 1:
        print("Number should be greater than Zero")
    elif isPerfectNumber(number) == True:
         print("Given number is perfect number")
    else:
        print("Given number is not a perfect number")


if __name__ == "__main__":
    main()