"""
Question: Write a program which accepts one number and checks whether it is prime or not.
Input: 11
Output: Prime Number

Hint: A prime number has exactly two distinct positive divisors: 1 and itself.
Primt numbers: 2, 3, 5, 7, 11, 13, 17

"""

def isNumberPrime(number):
        if number <= 1:
             return False
        if number == 2 or number == 3:
             return True
        for i in range(5, number + 1):
            if number % i == 0:
              return False
        return False

def main():
    numberToPass = int(input("Enter number: "))
    if isNumberPrime(numberToPass) == True:
        print("Number is Prime") 
    else:
        print("Number is not Prime")

if __name__ == "__main__":
    main()