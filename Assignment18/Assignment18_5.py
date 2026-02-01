"""
Docstring for Assignment18.Program_5

Question: 5.Write a program which accept N numbers from user and store it into List. Return addition of all 
prime numbers from that List. Main python file accepts N numbers from user and pass each 
number to ChkPrime() function which is part of our user defined module named as 
MarvellousNum. Name of the function from main python file should be ListPrime(). 
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 10 34 2 5 8
Output : 54 (13 + 5 + 7 + 2 + 5)
"""
import MarvellousNum
print('MarvellousNum Imported Successfully')



def main():
    add_prime_numbers = 0
    prime_list = MarvellousNum.ListPrime()
    for number in prime_list:
        add_prime_numbers = add_prime_numbers + number
    print("Addition of prime numbers from list is: ", add_prime_numbers)

if __name__ == "__main__":
    main()
 

    