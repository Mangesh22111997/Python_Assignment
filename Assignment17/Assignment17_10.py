"""
Docstring for Assignment17.Program_10

Question:
10. Write a program which accept number from user and return addition of digits in that number. 
Input : 5187934   
Output : 37
"""

def AddDigits(No):
    Sum = 0
    for i in str(No):
        Sum = Sum + int(i)
    return Sum

def main():
    Value = int(input("Enter a number: "))
    Ret = AddDigits(Value)
    print("Addition of digits is:", Ret)

if __name__ == "__main__":
    main()