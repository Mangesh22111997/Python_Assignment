
def CheckPrime(No):
    if No <= 1:
        print("It is not a Prime Number: ", No)

    for i in range(2, No):
        if (No % i) == 0:
            print('It is not a Prime Number: ', No)
        else:
            print('It is a Prime Number: ', No)
            return True

   
def ListPrime():
    number_of_element = int(input('Enter the number of elements: '))
    listData = []
    for i in range(number_of_element):
        listData.append(int(input(f"Please enter element at index {i}: ")))

    print("Original List is: ", listData)

    primeList = []
    
    primeList = list(filter(lambda No: CheckPrime(No) == True, listData))
        
    print("-------------primeList: ", primeList)
    return primeList


