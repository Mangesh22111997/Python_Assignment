"""
Docstring for Assignment19.Program_5

Question: 5.Write a program which contains filter(), map() and reduce() in it. Python application which 
contains one list of numbers. List contains the numbers which are accepted from user. Filter 
should filter out all prime numbers. Map function will multiply each number by 2. Reduce will 
return Maximum number from that numbers. (You can also use normal functions instead of 
lambda functions). 
Input List = [2, 70 , 11, 10, 17, 23, 31, 77] 
List after filter = [2, 11, 17, 23, 31] 
List after map = [4, 22, 34, 46, 62] 
Output of reduce = 62 
"""

from functools import reduce

def is_prime(no):
    if no < 2:
        return False
    for i in range(2, no):
        if no % i == 0:
            return False
    return True


# ...existing code...

def main():
    number_of_element = int(input("Enter number of Elements: "))

    listdata = []
    for i in range(number_of_element):
        listdata.append(int(input(f"Please enter element at index {i}: ")))

    # Filter
    
    filteredlist = list(filter(lambda no: is_prime(no), listdata))
    print("List after filter: ", filteredlist)

    # Map
    mappedlist = list(map(lambda no: no * 2, filteredlist))
    print("List after map: ", mappedlist)

    # Reduce
    reducedvalue = reduce(lambda no1, no2: no1 if no1 > no2 else no2, mappedlist)
    print("Output of reduce: ", reducedvalue)

if __name__ == "__main__":
    main()