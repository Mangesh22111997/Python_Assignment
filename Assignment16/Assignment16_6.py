"""
Docstring for Assignment16.Program_6

Question: 6.Write a program which accept number from user and check whether that number is positive or 
negative or zero. 
Input : 11    
Output : Positive Number 
Input : -8    
Input : 0    
Input : 25    
Output : Zero 
Output : Negative Number 

"""

def CheckNumber(Number):
    if Number > 0:
        print("Positive Number")
    elif Number < 0:
        print("Negative Number")
    else:
        print("Zero")

def main():
    CheckNumber(11)
    CheckNumber(-8)
    CheckNumber(0)
    CheckNumber(25)

if __name__ == "__main__":
    main()