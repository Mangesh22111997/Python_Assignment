"""
Docstring for Assignment16.Program_9

Question: 9. Write a program which display first 10 even numbers on screen. 
Output :  
4 
6 
8 
10 
12 
14 
16 
18 
20 

"""
def DisplayEven(No):
    for i in range(1, No + 1):
        if i % 2 == 0:
            print(i)

def main():
    DisplayEven(20)

if __name__ == "__main__":
    main()