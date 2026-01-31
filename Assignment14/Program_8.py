"""
Docstring for Assignment14.Program_8

Question 8. Write a lambda function which accepts two numbers and returns addition.

"""
num_add = lambda No1, No2: No1 + No2

def main():
    No1 = int(input("Enter first number: "))
    No2 = int(input("Enter second number: "))
    sum = num_add(No1, No2)
    print("Sum of two numbers is:", sum)

if __name__ == "__main__":
    main()