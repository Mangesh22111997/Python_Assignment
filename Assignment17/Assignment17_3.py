"""
Docstring for Assignment17.Program_3

Question:
3. Write a program which accept one number from user and return its factorial. 
Input :  5
Output : 120 

"""
def Factorial(No):
    Fact = 1
    for i in range(1, No + 1):
        Fact = Fact * i
    print("Factorial is:", Fact)

    
def main():
    No = int(input("Enter a number to find its factorial: "))
    Factorial(No)


if __name__ == "__main__":
    main()