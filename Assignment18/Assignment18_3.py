"""
Docstring for Assignment18.Program_3

Question: 3.Write a program which accept N numbers from user and store it into List. Return Minimum 
number from that List. 
Input : Number of elements : 4 
Input Elements : 13 5 45 7
Output : 5 

"""

def getminnumberfromlist(listData):
    minimum = listData[0]
    
    for i in range(len(listData)):
        if listData[i] < minimum:
            minimum = listData[i]
    return minimum

def main():
    number_of_element = int(input("Enter number of Elements: "))

    listdata = []
    for i in range(number_of_element):
        listdata.append(int(input(f"Please enter element at index {i}: ")))
    print("Minimum number from list is: ", getminnumberfromlist(listdata))

if __name__ == "__main__":
    main()