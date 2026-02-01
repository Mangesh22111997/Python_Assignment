"""
Docstring for Assignment19.Program_4

Question: 4.Write a program which contains filter(), map() and reduce() in it. Python application which 
contains one list of numbers. List contains the numbers which are accepted from user. Filter 
should filter out all such numbers which are even. Map function will calculate its square. 
Reduce will return addition of all that numbers. 
Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10] 
List after filter = [2, 4, 4, 2, 8, 10] 
List after map = [4, 16, 16, 4, 64, 100] 
Output of reduce = 204 
"""

from functools import reduce


def main():
    number_of_element = int(input("Enter number of Elements: "))

    listdata = []
    for i in range(number_of_element):
        listdata.append(int(input(f"Please enter element at index {i}: ")))

    # Filter
    filteredlist = list(filter(lambda no: no % 2 == 0, listdata))
    print("List after filter: ", filteredlist)

    # Map
    mappedlist = list(map(lambda no: no ** 2, filteredlist))
    print("List after map: ", mappedlist)

    # Reduce
    reducedvalue = reduce(lambda no1, no2: no1 + no2, mappedlist)
    print("Output of reduce: ", reducedvalue)

if __name__ == "__main__":
    main()