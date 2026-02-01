"""
Docstring for Assignment16.Program_8

Question: 8. Write a program which accept number from user and print that number of “*” on screen. 
Input : 5    
Output : * * * * * 

"""
def DisplayStars(No):
    for i in range(No):
        print("*", end=" ")
    

def main():
    DisplayStars(5)

if __name__ == "__main__":
    main()