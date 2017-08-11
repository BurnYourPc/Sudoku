import os
import numpy as np
from copy import deepcopy
from tkinter import *
import tkinter.messagebox
from src.burnImage import burnSudo2Img as BS
from src.generators import Generators as Gen
from src.utils import GeneratorUtils as GU
from src.ratingSudos import rating as RT
from src.checkers import SudoCheck as SC
from src.solver import solver as SL


def gen_save(num,sym,sourceimg,destination):
    num1=0
    num2=0
    num3=0
    num4=0
    num5=0
    if (sym):
        for i in range(num):
            A=Gen.GenerateProb(0,0,i%11+1)
            lvl=RT.RateProb(A)
            print(i+1)
            if (lvl==1):
                destination2=destination+"VeryEasy"
                num1=num1+1
            elif (lvl==2):
                destination2=destination+"Easy"
                num2=num2+1
            elif (lvl==3):
                destination2=destination+"Medium"
                num3=num3+1
            elif (lvl==4):
                destination2=destination+"Hard"
                num4=num4+1
            else:
                destination2=destination+"VeryHard"
                num5=num5+1
            
            BS.CreateSudoImg(A,sourceimg,destination2)
    
    else:
        for i in range(num):
            A=Gen.GenerateProb(22,32,0)          # 22 to 32 knokn cells
            lvl=RT.RateProb(A)
            print(i+1)
            if (lvl==1):
                destination2=destination+"VeryEasy"
                num1=num1+1
            elif (lvl==2):
                destination2=destination+"Easy"
                num2=num2+1
            elif (lvl==3):
                destination2=destination+"Medium"
                num3=num3+1
            elif (lvl==4):
                destination2=destination+"Hard"
                num4=num4+1
            else:
                destination2=destination+"VeryHard"
                num5=num5+1
            
            BS.CreateSudoImg(A,sourceimg,destination2)
    
    print(" ")
    print(num1,"very Easy, ",num2,"Easy, ",num3,"Medium, ",num4,"Hard and ",num5,"very Hard sudoku generated")


def CreatePdf(nums,sym,path):
    if (sym==1):
        path2=path+"SudoProblems/Symmetrical/"
    else:
        path2=path+"SudoProblems/NonSymmetrical/"
    
    source=path+"src/main"
    destination=path+"SudoProblems/SudoPdf"
    BS.CreateSudoPdf(nums,path2,source,destination)


def printMes(title,text):
    tkinter.messagebox.showinfo(title,text)


def solvegui():
    mw = Tk()
    mw.title("Solve Sudoku problem")
    rows = []
    for i in range(9):
        cols = []
        for j in range(9):
            e = Entry(relief=RIDGE,bd=5,width=3)
            e.grid(row=i+1, column=j+1, sticky=NSEW)
            e.insert(END, '%d' % 0)
            cols.append(e)
        rows.append(cols)
    
    def onPressSolve():
        A=np.zeros((9,9), dtype=int)
        i=0
        for row in rows:
            j=0
            for col in row:
                A[i,j]=int(col.get())
                j=j+1
            i=i+1
        if (np.min(A)>=0 and np.max(A)<=9):
            if (SC.IsSudoRight(A)):
                printMes("Solver","Already Solved!")
            else:
                Adef=deepcopy(A)
                if (GU.CountSolutions(Adef,[],0,1)==1):
                    A=SL.SudoSolveIt2(A,[],1)
                    print(A)
                else:
                    printMes("Solver","There isn't unique solution!")
        else:
            printMes("Solver","Wrong inputs!")
    
        mw.destroy()
    
    Button(text='give Sudoku', command=onPressSolve).grid()
    mainloop()


def rategui():
    mw = Tk()
    mw.title("Rate Sudoku problem")
    rows = []
    for i in range(9):
        cols = []
        for j in range(9):
            e = Entry(relief=RIDGE,bd=5,width=3)
            e.grid(row=i+1, column=j+1, sticky=NSEW)
            e.insert(END, '%d' % 0)
            cols.append(e)
        rows.append(cols)
    
    def onPressRate():
        A=np.zeros((9,9), dtype=int)
        i=0
        for row in rows:
            j=0
            for col in row:
                A[i,j]=int(col.get())
                j=j+1
            i=i+1
        if (np.min(A)>=0 and np.max(A)<=9):
            if (SC.IsSudoRight(A)):
                printMes("Rating","Already Solved!")
            else:
                Adef=deepcopy(A)
                if (GU.CountSolutions(Adef,[],0,1)==1):
                    diff=RT.RateProb(A)
                    printMes("Rating","Your Problem is "+BS.getStrDiff(difficulty))
                else:
                    printMes("Rating","There isn't unique solution!")
        else:
            printMes("Rating","Wrong inputs!")
    
        mw.destroy()
    
    Button(text='give Sudoku', command=onPressRate).grid()
    mainloop()


#-----------------------------------------------------------------------------------#


print("Welcome to Sudoku Project by BurnYourPc Organization!")
print(" ")
print("Choose what to do...")
print("1. Generate more Sudoku problems [press -g number_of_problems]")
print("2. Create Pdf with Sudoku problems [press -pdf]")
print("3. Solve Sudoku Problem [press -solve]")
print("4. Rate Sudoku Problem [press -rate]")
print("5. exit [press exit]")
choice = input()

path=os.path.dirname(os.path.abspath("."))

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
    answ=input("Symmetrical[1] or NonSymmetrical[2]?\n")
    answ=int(answ)
	
    if (answ!=1 and answ!=2):
        print("Wrong Input!")
    else:
        ve=input("How many Very Easy?\n")
        nums.append(int(ve))
    
        ve=input("How many Easy?\n")
        nums.append(int(ve))
    
        ve=input("How many Medium?\n")
        nums.append(int(ve))
    
        ve=input("How many Hard?\n")
        nums.append(int(ve))
    
        ve=input("How many Very Hard?\n")
        nums.append(int(ve))
        print(" ")
        
        if (answ==1):
            sym=1
            
        else:
            sym=2
        
        CreatePdf(nums,sym,path[0:len(path)-3])
        destination=path[0:len(path)-3]+"SudoProblems/SudoPdf"
        file_list = os.listdir(destination)
        file_count = len(file_list)
        name="SudokuProblems"+str(file_count)+".pdf"
        print("Your Pdf is "+name+" in SudoProblems/SudoPdf folder")

elif (choice[0:6]=="-solve"):
    solvegui()

elif (choice[0:5]=="-rate"):
    rategui()

elif (choice=="exit"):
    print("Bye Bye!")

else:
    print("Wrong inputs! Try again...")
