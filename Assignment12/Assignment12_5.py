"""
Question: Write a program which accepts one number and prints that many numbers in reverse order.
Input: 5
Output: 54321

"""


def displayReverOf(number):
    result = ""
    for i in range(number, 0, -1):
      result = result + str(i)

    return result

def main():
    numberToPass = int(input("Enter number: "))
    print(displayReverOf(numberToPass)) 

if __name__ == "__main__":
    main()