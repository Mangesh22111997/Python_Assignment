
"""
Docstring for Assignment14.Program_2
Question: 2. Write a lambda function which accepts one number and returns cube of that number.

"""

cubeofnumber = lambda num : num * num * num
def main():
    number = float(input('Enter a number: '))
    cube = cubeofnumber(number)
    print("Cube of number is:", cube)

if __name__ == "__main__":
    main()
