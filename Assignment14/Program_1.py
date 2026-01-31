"""
Docstring for Assignment14.Program_1
Question: 1. Write a lambda function which accepts one number and returns square of that number.


"""
squareofnumber = lambda num: num * num

def main():
    number = int(input('Enter a number: '))
    square = squareofnumber(number)
    print("Square of number is:", square)

if __name__ == "__main__":
    main()