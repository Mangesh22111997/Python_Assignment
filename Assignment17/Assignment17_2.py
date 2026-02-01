"""
Docstring for Assignment17.Program_2

Question:    
2. Write a program which accept one number and display below pattern. 
Input :  5
Output :  
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * *  
"""

def DisplayPattern(No):
    for i in range(No):
        for j in range(No):
            print("*", end=" ")
        print()

def main():
    print("Enter number of rows and columns: ")
    Value = int(input())

    DisplayPattern(Value)


if __name__ == "__main__":
    main()