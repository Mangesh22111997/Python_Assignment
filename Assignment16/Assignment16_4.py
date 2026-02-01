"""
Docstring for Assignment16.Program_4

Question: 4.Write a program which display 5 times Marvellous on screen. 
Output : 
Marvellous 
Marvellous 
Marvellous 
Marvellous 
Marvellous 

"""
def Display(Name, No):
    for i in range(No):
        print(Name)

def main():
    Display('Marvellous', 5)

if __name__ == "__main__":
    main()