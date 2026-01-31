"""
Docstring for Assignment14.Program_6

Question 6. Write a lambda function which accepts one number and returns True if number is odd 
otherwise False.

"""
odd_number = lambda num: True if num % 2 != 0 else False

def main():
    No = int(input('Enter number: '))
    is_odd = odd_number(No)
    print("Is number odd?", is_odd)


if __name__ == "__main__":
    main()