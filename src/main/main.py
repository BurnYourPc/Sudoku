import os
from src.burnImage import burnSudo2Img as BS
from src.generators import Generators as Gen
from src.ratingSudos import rating as RT


def gen_save(num,sym,sourceimg,destination):
    if (sym):
        for i in range(num):
            A=Gen.GenerateProb(0,0,i%11+1)
            lvl=RT.RateProb(A)
            if (lvl==1):
                destination2=destination+"VeryEasy"
            elif (lvl==2):
                destination2=destination+"Easy"
            elif (lvl==3):
                destination2=destination+"Medium"
            elif (lvl==4):
                destination2=destination+"Hard"
            else:
                destination2=destination+"VeryHard"
            
            BS.CreateSudoImg(A,sourceimg,destination2)
    
    else:
        for i in range(num):
            A=Gen.GenerateProb(23,34,0)
            lvl=RT.RateProb(A)
            if (lvl==1):
                destination2=destination+"VeryEasy"
            elif (lvl==2):
                destination2=destination+"Easy"
            elif (lvl==3):
                destination2=destination+"Medium"
            elif (lvl==4):
                destination2=destination+"Hard"
            else:
                destination2=destination+"VeryHard"
            
            BS.CreateSudoImg(A,sourceimg,destination2)


print("Welcome to Sudoku Project by BurnYourPc Organization!")
print(" ")
print("Choose what to do...")
print("1. Generate more Sudoku problems [press -g number_of_problems]")
print("2. Create Pdf with Sudoku problems [press -pdf]")
print("3. exit [press exit]")
choice = input()

path=os.path.dirname(os.path.abspath("."))
print(path)
if choice[0:2]=="-g":
	num=int(choice[3:len(choice)])
	answ=input("Symmetrical[1] or NonSymmetrical[2]?\n")
	answ=int(answ)
	sourceimg=path+"/burnImage"
	if (answ==1):
	    destination=path[0:len(path)-3]+"SudoProblems/Symmetrical/"
	    gen_save(num,True,sourceimg,destination)
	elif(answ==2):
	    destination=path[0:len(path)-3]+"SudoProblems/NonSymmetrical/"
	    gen_save(num,False,sourceimg,destination)
	else:
	    print("Wrong input!")
	    
elif (choice[0:4]=="-pdf"):
    nums=[]
    ve=input("How many Very Easy?")
    nums.append(int(ve))
    
    ve=input("How many Easy?")
    nums.append(int(ve))
    
    ve=input("How many Medium?")
    nums.append(int(ve))
    
    ve=input("How many Hard?")
    nums.append(int(ve))
    
    ve=input("How many Very Hard?")
    nums.append(int(ve))
    
    
    
    
elif (choice=="exit"):
    print("Bye Bye!")
else:
    print("Wrong inputs! Try again...")
