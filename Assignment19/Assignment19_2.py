"""
Docstring for Assignment19.Program_2

Question: 2.Write a program which contains one lambda function which accepts two parameters and return 
its multiplication. 
Input : 4 3
Input : 6 3

Output : 12 
Output : 18
"""

productoftwo = lambda no1, no2: no1 * no2

def main():
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    result = productoftwo(number1, number2)
    print("Product of two numbers is: ", result)

if __name__ == "__main__":
    main()