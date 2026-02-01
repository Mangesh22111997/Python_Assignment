"""
Docstring for Assignment18.Program_1

Question: .Write a program which accept N numbers from user and store it into List. Return addition of all 
elements from that List. 
Input : Number of elements : 6 
Input Elements : 13 5 45 7 4 56
Output : 130
"""


def getSumOfElements(listData):
    sum = 0
    for i in range(len(listData)):
        sum = sum + listData[i]

    return sum

def main():
    number = int(input("Enter number of elements: "))
    listData = []

    for i in range(number):
        listData.append(int(input(f"Please enter element at index {i}: ")))
    
    print("Total Sum of elements: ", getSumOfElements(listData))

if __name__ == "__main__":
    main()
