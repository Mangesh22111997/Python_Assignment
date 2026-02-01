"""
Docstring for Assignment17.Program_5

Question: 5.Write a program which accept one number for user and check whether number is prime or not. 
Input :  5
Output : It is Prime Number 
"""

def CheckPrime(No):
    if No <= 1:
        print("It is not a Prime Number: ", No)

    for i in range(2, No):
        if (No % i) == 0:
            print('It is not a Prime Number: ', No)
        else:
            print('It is a Prime Number: ', No)

def main():
    CheckPrime(11)
    CheckPrime(10)
    CheckPrime(1)
    CheckPrime(0)
    CheckPrime(-7)


if __name__ == "__main__":
    main()