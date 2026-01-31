"""
Docstring for Assignment14.Program_9

Question 9. Write a lambda function which accepts two numbers and returns multiplication.

"""
num_mul = lambda No1, No2: No1 * No2

def main():
    No1 = int(input("Enter first number: "))
    No2 = int(input("Enter second number: "))
    product = num_mul(No1, No2)
    print("Product of two numbers is:", product)

if __name__ == "__main__":
    main()