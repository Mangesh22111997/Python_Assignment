"""
Docstring for Assignment14.Program_4

Question 4. Write a lambda function which accepts two numbers and returns minimum number.

"""
min_number = lambda No1, No2: No1 if No1 < No2 else No2

def main():
    No1 = int(input('Enter first number: '))
    No2 = int(input('Enter second number: '))
    minimum = min_number(No1, No2)
    print("Minimum number is:", minimum)

if __name__ == "__main__":
    main()