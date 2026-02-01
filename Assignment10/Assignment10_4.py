"""
Question: Write a program which accepts one number and prints all even numbers till that number.

Input: 10
Output: 2 4 6 8 10

"""

def getEvenNumbersUntil(number):
    result = []
    
    for i in range(1, number + 1):
        if i % 2 == 0:
            result.append(i)
    
    return result

def main():
    numberToPass = int(input("Enter number: "))
    
    if numberToPass <= 0:
        print("Error: Number must be greater than 1") 
    elif getEvenNumbersUntil(numberToPass) == []:
        print("No even numbers are avaiable")
    else:
        print("Even numbers are: ", *getEvenNumbersUntil(numberToPass) ) # This approach utilizes the * operator to unpack the list elements directly into the print function, which by default separates items with spaces.

if __name__ == "__main__":
    main()