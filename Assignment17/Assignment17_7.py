"""
Docstring for Assignment17.Program_7

Question: 7.  Write a program which accept one number and display below pattern. 
Input :  5
Output : 
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""

def DisplayPattern(No):
    for i in range(No):
        for j in range(1, No + 1):
            print(j, end = " ")
        print()


def main():
    print("Enter number of rows and columns: ")
    Value = int(input())

    DisplayPattern(Value)

if __name__ == "__main__":
    main()