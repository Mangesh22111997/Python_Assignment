"""
Docstring for Assignment16.Program_7

Question: 
7. Write a program which contains one function that accept one number from user and returns 
true if number is divisible by 5 otherwise return false. 
Input : 8    
Output : False 
Output : True 

"""

def DivisibleByFive(Number):
    if Number % 5 == 0:
        return True
    else:
        return False
    
def main():
    Ret = DivisibleByFive(8)
    print("Is 8 divisible by 5?:", Ret)

    Ret = DivisibleByFive(25)
    print("Is 25 divisible by 5?:", Ret)

if __name__ == "__main__":
    main()