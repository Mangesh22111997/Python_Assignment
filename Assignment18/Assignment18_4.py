"""
Docstring for Assignment18.Program_4

Question: 4.Write a program which accept N numbers from user and store it into List. Accept one another 
number from user and return frequency of that number from List. 
Input : Number of elements : 11 
Input Elements : 13 5 45 7 4 56 5 34 2 5 65
Element to search : 5 
Output : 3 
"""

def getfrequencyofnumber(listData, searchnumber):
    frequency = 0
    for i in range(len(listData)):
        if listData[i] == searchnumber:
            frequency += 1
    return frequency


def main():
    number_of_element = int(input('Enter the number of elements: '))
    listdata = []
    for i in range(number_of_element):
        listdata.append(int(input(f"Please enter element at index {i}: ")))

    searchnumber = int(input("Element to search : "))

    print("Frequency of number from list is: ", getfrequencyofnumber(listdata, searchnumber))

if __name__ == "__main__":
    main()