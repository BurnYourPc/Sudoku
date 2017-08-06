import numpy as np
from copy import deepcopy
from src.utils import SolverUtils as SV
from src.utils import GeneratorUtils as GU
from src.checkers import SudoCheck as SC
from src.solver import solver as SL
from src.burnImage import burnSudo2Img as BS
from src.generators import Generators as Gen
from random import randint
from PyPDF2 import PdfFileWriter, PdfFileReader
import os

B1=np.array([[1,4,0,0,0,0,0,0,0],[0,0,5,4,7,1,0,0,0],[0,0,7,5,0,0,0,0,9],[0,6,1,7,0,5,3,8,0],[0,7,8,1,0,3,6,9,0],[0,5,9,6,0,8,7,2,0],[5,0,0,0,0,7,2,0,0],[0,0,0,3,8,4,1,0,0],[0,0,0,0,0,0,0,3,7]])
B2=np.array([[0,0,0,0,9,0,7,0,8],[0,0,0,8,0,0,0,0,0],[5,1,0,6,0,7,0,0,0],[0,0,9,2,0,0,0,8,0],[6,0,0,0,0,0,0,0,4],[0,7,0,0,0,1,5,0,0],[0,0,0,5,0,9,0,6,1],[0,0,0,0,0,8,0,0,0],[2,0,3,0,7,0,0,0,0]])


#C=SV.ConstructC(B1)
#SV.multLineEr(C)
#print(" ")
#print(" ")
# Solve B1,B2 with the fastest solver implemented
#A1=SL.SudoSolveIt(B1,[],1)
A2=SL.SudoSolveIt(B2,[],1)
print(A2)
print(SC.IsSudoRight(A2))
print(" ")
#Creating NonSymmetrical Problem with 23 known numbers
#matrix=Gen.RandGenerator3([],23,1,[])
#BS.CreateSudoImg(matrix,False)

#matrix=Gen.RandGenerator3([],23,1,[])
#BS.CreateSudoImg(matrix,False,"/fuul_path_to(image.pdf)/src/burnImage","/full_path_to_destination_folder")

f=np.array([2,2,2])
print(np.unique(f))
print(np.unique(f).size==1)
d=np.array([[1,2,3],[5,6,7],[23,6,1],[67,8,1]])
print(d)
g=np.array([[0,0,0],[0,0,0]])
d[d[:,1]==6,:]=g
print("d")
print(d)
h=np.array([1,2,3,4,5,6,7,0,9])
d=np.unique(h)
print(d)
print(np.array(np.where(d==0)))
x=np.array(np.where(d==0))
d=np.delete(d,np.array(np.where(d==0)))
print(d)
#c=d[g!=0,1]
print(h[0:9])
if(np.array_equal(g[0:10],h[0:11])):
    print("hello")
#for i in xrange(1,8,3):
#    for j in xrange(i,i+2,1):
#        for k in xrange(j+1,i+3,1):
#            print(j,k)
#            print(i)
#            print("third ",SV.getThirdBox(i,j,k,1))
            
#print(" ")
#for i in xrange(1,4,1):
#    for j in xrange(i,i+7,3):
#        for k in xrange(j+3,i+7,3):
#            print(j,k)
#            print(i)
#            print("third ",SV.getThirdBox(i,j,k,2))
#Creating Symmetrical Problems (symemetry is a number from 1 to 15, but 1-11 is efficient)
#matrix=Gen.GenSymmetrical(5)
#BS.CreateSudoImg(matrix,True)
#matrix=Gen.GenSymmetrical(2)
#BS.CreateSudoPdf(32,'/full_path_to_problems_png',False_for_nonSym_Tru_for_Sym,'/full_path_to/src/examples','/full_path_to_destination_folder_for_pdf')

