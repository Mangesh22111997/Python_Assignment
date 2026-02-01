"""
Docstring for Assignment18.Program_2

Question: 2.Write a program which accept N numbers from user and store it into List. Return Maximum 
number from that List. 
Input : Number of elements : 7 
Input Elements : 13 5 45 7 4 56 34
Output : 56 
"""

def getmaxnumberfromlist(listData):
    maximum = listData[0]
    
    for i in range(len(listData)):
        if listData[i] > maximum:
            maximum = listData[i]
    return maximum

def main():
    number_of_element = int(input("Enter number of Elements: "))

    listdata = []
    for i in range(number_of_element):
        listdata.append(int(input(f"Please enter element at index {i}: ")))
    print("Maximum number from list is: ", getmaxnumberfromlist(listdata))

if __name__ == "__main__":
    main()