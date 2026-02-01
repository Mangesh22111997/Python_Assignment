"""
Docstring for Assignment19.Program_3

Question: 3.Write a program which contains filter(), map() and reduce() in it. Python application which 
contains one list of numbers. List contains the numbers which are accepted from user. Filter 
should filter out all such numbers which greater than or equal to 70 and less than or equal to 
90. Map function will increase each number by 10. Reduce will return product of all that 
numbers. 
Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70] 
List after filter = [76, 89, 86, 90, 70] 
List after map = [86, 99, 96, 100, 80] 
Output of reduce = 6538752000
"""
from functools import reduce


def main():
    number_of_element = int(input("Enter number of Elements: "))

    listdata = []
    for i in range(number_of_element):
        listdata.append(int(input(f"Please enter element at index {i}: ")))

    # Filter
    filteredlist = list(filter(lambda no: no >= 70 and no <= 90, listdata))
    print("List after filter: ", filteredlist)

    # Map
    mappedlist = list(map(lambda no: no + 10, filteredlist))
    print("List after map: ", mappedlist)

    # Reduce
    reducedvalue = reduce(lambda no1, no2: no1 * no2, mappedlist)
    print("Output of reduce: ", reducedvalue)

if __name__ == "__main__":
    main()