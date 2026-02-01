"""
Docstring for Assignment17.Program_9

Question: 9. Write a program which accept number from user and return number of digits in that number. 
Input : 5187934   
Output : 7 
"""

def countDigits(No):
    No = str(No)
    Count = 0
    for i in No:
        Count += 1
    return Count

def main():
    Value = int(input("Enter a number: "))
    Ret = countDigits(Value)
    print("Number of digits are:", Ret)

if __name__ == "__main__":
    main()