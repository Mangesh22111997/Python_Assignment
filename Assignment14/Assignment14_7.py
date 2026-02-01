"""
Docstring for Assignment14.Program_7

Question 7. Write a lambda function which accepts one number and returns True if divisible by 5.

"""
number_divisible_by_5 = lambda num: True if num % 5 == 0 else False
def main():
    No = int(input('Enter number: '))
    is_divisible_by_5 = number_divisible_by_5(No)
    print("Is number divisible by 5?", is_divisible_by_5)

    
if __name__ == "__main__":
    main()