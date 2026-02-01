"""
Docstring for Assignment14.Program_10

Question 10. Write a lambda function which accepts three numbers and returns largest number

"""
largest_number = lambda No1, No2, No3: No1 if (No1 > No2 and No1 > No3) else (No2 if No2 > No3 else No3)

def main():
    No1 = int(input("Enter first number: "))
    No2 = int(input("Enter second number: "))
    No3 = int(input("Enter third number: "))
    largest = largest_number(No1, No2, No3)
    print("Largest number is:", largest)
    

if __name__ == "__main__":
    main()