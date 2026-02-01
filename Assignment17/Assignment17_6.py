"""
Docstring for Assignment17.Program_6

Question: 6. Write a program which accept one number and display below pattern. 
Input :  5
Output : 
* * * * *
* * * * 
* * *
* *
*
"""

def DisplayPattern(No):
    for i in range(No, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

def main():
    print("Enter number of rows: ")
    Value = int(input())

    DisplayPattern(Value)

if __name__ == "__main__":
    main()