"""
Question: Write a program which accepts one number and prints sum of first N natural numbers.

Input: 5
Output: 15

"""

def getSumOfFirstNnumbers(number):
    sum = 0
    for i in range(1, number + 1):
        sum = sum + i
    
    return sum

def main():
    numberToPass = int(input("Enter number: "))
    print("Sum of numbers is: ", getSumOfFirstNnumbers(numberToPass) ) 

if __name__ == "__main__":
    main()