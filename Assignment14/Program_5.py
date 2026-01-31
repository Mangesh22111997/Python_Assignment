"""
Docstring for Assignment14.Program_5

Question 5. Write a lambda function which accepts one number and returns True if number is even 
otherwise False.

"""

even_number = lambda num: True if num % 2 == 0 else False

def main():
    No = int(input('Enter number: '))
    is_even = even_number(No)
    print("Is number even?", is_even)

if __name__ == "__main__":
    main()