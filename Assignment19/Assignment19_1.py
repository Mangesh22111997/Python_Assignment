"""
Docstring for Assignment19.Program_1

Question: 1.Write a program which contains one lambda function which accepts one parameter and return  
power of two. 
Input : 4  Output : 16
Input : 6  Output : 64 
 

"""

poweroftwo = lambda no: no ** 2

def main():
    number = int(input("Enter number: "))
    result = poweroftwo(number)
    print("Power of two is: ", result)

if __name__ == "__main__":
    main()