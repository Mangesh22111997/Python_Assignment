"""
Question: Write a program which accepts one number and prints factorial of that number.
Input: 5
Output: 120

"""

def getFactorialOf(number):
    result = 1
    for i in range(1, number + 1):
        result = result * i
    
    return result

def main():
    numberToPass = int(input("Enter number: "))
    
    if numberToPass <= 0:
        print("Error: Number must be greater than 1") 
    else:
        print("Sum of numbers is: ", getFactorialOf(numberToPass) ) 

if __name__ == "__main__":
    main()