"""
Docstring for Assignment16.Program_3

Question: 3. Write a program which contains one function named as Add() which accepts two numbers 
from user and return addition of that two numbers. 
Input : 11    5   
Output : 16 

"""
def add(No1, No2):
    Result = No1 + No2
    print("Addition is:", Result)

def main():
    add(10, 12)
    add(21,22)

if __name__ == "__main__":
    main()