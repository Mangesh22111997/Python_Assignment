"""
Question: 5. Write a program which accepts one number and prints all odd numbers till that number.

Input: 10
Output: 1 3 5 7 9

"""

def getOddNumbersUntil(number):
    result = []
    
    for i in range(1, number + 1):
        if i % 2 != 0:
            result.append(i)
    
    return result

def main():
    numberToPass = int(input("Enter number: "))
    
    if numberToPass <= 0:
        print("Error: Number must be greater than 1") 
        return
    
    result = getOddNumbersUntil(numberToPass)

    if result == []:
        print("No odd numbers are avaiable")
    else:
        print("odd numbers are: ", *result) # This approach utilizes the * operator to unpack the list elements directly into the print function, which by default separates items with spaces.

if __name__ == "__main__":
    main()