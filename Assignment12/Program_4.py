"""
Question: Write a program which accepts one number and prints that many numbers starting from 1.
Input: 5
Output: 1 2 3 4 5

"""


def displayNumberUntil(number):
    for i in range(1, number + 1):
        print(i)

def main():
    number = int(input("Enter number: "))
    displayNumberUntil(number)

if __name__ == "__main__":
    main()