"""
Docstring for Assignment17.Program_4

Question:  
4.Write a program which accept one number form user and return addition of its factors. 
Input :  12
Output : 16  
5   
(1+2+3+4+6) 

"""
def AddFactors(No):
    Sum = 0
    for i in range(1, No):
        if (No % i) == 0:
            # print(f'no: {No} i: {i}')
            # print(Sum)
            Sum = Sum + i
            #print(f'After adding {i}, Sum is now: {Sum}')
    print("Addition of factors is:", Sum)

def main():
    AddFactors(12)

if __name__ == "__main__":
    main()