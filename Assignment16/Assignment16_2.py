"""
Docstring for Assignment16.Program_2

Question: 2. Write a program which contains one function named as ChkNum() which accept one 
parameter as number. If number is even then it should display “Even number” otherwise 
display “Odd number” on console. 
Input : 11    
Output : Odd Number 
Input : 8    
Output : Even Number 
"""

def ChkNum(Number):
    if Number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")


def main():
    ChkNum(11)
    ChkNum(8)

if __name__ == "__main__":
    main()