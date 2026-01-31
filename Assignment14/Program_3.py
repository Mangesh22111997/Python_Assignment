"""
Docstring for Assignment14.Program_3


Question 3. Write a lambda function which accepts two numbers and returns maximum number.

"""
max_number = lambda No1, No2: No1 if No1 > No2 else No2

def main():
    No1 = int(input('Enter first number: '))
    No2 = int(input('Enter second number: '))
    maximum = max_number(No1, No2)
    print("Maximum number is:", maximum)

if __name__ == "__main__":
    main()