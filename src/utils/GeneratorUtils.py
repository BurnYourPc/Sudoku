import numpy as np
from copy import deepcopy
from . import SolverUtils as SV
from src.checkers import SudoCheck as SC
from random import randint


def CountSolutions(A,C,numSol,n):
    Arec = deepcopy(A)
    Crec = deepcopy(C)
    if n==1:
        Crec=SV.ConstructC(Arec)
        return CountSolutions(Arec,Crec,numSol,n+1)
    else:
        if (n==2):
            Arec, Crec, DidIn = SV.SudoInput1(Arec,Crec)
            Arec, Crec, DidIn = SV.SudoInput2(Arec,Crec)
            return CountSolutions(Arec,Crec,numSol,n+1)
        if np.min(Arec)>0:
            numSol=numSol+1
            return numSol
        if (SC.IsDeadEnd(Crec)):
            return numSol
        Arec, Crec, DidIn = SV.SudoInput1(Arec,Crec)
        if (DidIn):
            if (SC.IsDeadEnd(Crec)):
                return numSol
            else:
                Arec, Crec, DidIn = SV.SudoInput2(Arec,Crec)
                return CountSolutions(Arec,Crec,numSol,n)
        else:
            Arec, Crec, DidIn = SV.SudoInput2(Arec,Crec)
            if (DidIn):
                return CountSolutions(Arec,Crec,numSol,n)
        r=SV.FindMinRow(Crec)
        rC=Crec[r,:]
        for i in range(9):
            if (rC[i]>0):
                A2=deepcopy(Arec)
                C2=deepcopy(Crec)
                A2[rC[9],rC[10]]=rC[i]
                C2=SV.clearC(C2,rC[9],rC[10],rC[11],rC[i])
                C2=np.delete(C2,r,0)
                numSol=CountSolutions(A2,C2,numSol,n+1)
                if numSol==2:
                    return numSol
        return numSol


def makeNewSudo(A,n):    #Generate a full Sudoku grid
    Arec=deepcopy(A)
    if (np.min(Arec)>0):
        return Arec
    for i in range(9):
        for j in range(9):
            if (Arec[i,j]==0):
                posnum=SV.FindPosNums(Arec,i,j)
                while (posnum.size>0):
                    pick=randint(0, posnum.size-1)
                    Arec[i,j]=posnum[pick]
                    A2=makeNewSudo(Arec,n+1)
                    if (np.min(A2)>0):
                        return A2
                    posnum=np.delete(posnum,pick)
                return Arec


def giveSymMat(symmetry):       #Store the symmetrical patterns
    A=np.zeros((9,9), dtype=int)
    
    if(symmetry==1):
        pos=np.array([[0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,5,5,5,6,6,6,6,6,7,7,7,7,7,8,8,8],[5,6,7,0,1,2,5,7,0,2,5,6,7,0,1,2,6,7,8,1,2,3,6,8,1,3,6,7,8,1,2,3]])
        for i in range(32):
            A[pos[0,i],pos[1,i]]=1
    
    elif(symmetry==2):
        pos=np.array([[0,0,0,1,1,1,1,2,2,2,3,3,3,4,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8],[0,1,4,0,3,4,5,1,2,7,0,4,8,0,3,5,8,0,4,8,1,6,7,3,4,5,8,4,7,8]])
        for i in range(30):
            A[pos[0,i],pos[1,i]]=1
            
    elif (symmetry==3):
        pos=np.array([[0,0,0,0,1,1,1,2,2,2,2,3,3,3,5,5,5,6,6,6,6,7,7,7,8,8,8,8],[1,2,6,7,0,6,8,0,1,5,8,2,3,5,3,5,6,0,3,7,8,0,2,8,1,2,6,7]])
        for i in range(28):
            A[pos[0,i],pos[1,i]]=1
            
    elif (symmetry==4):
        pos=np.array([[0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8],[4,1,3,5,7,2,3,5,6,1,2,6,7,0,8,1,2,6,7,2,3,5,6,1,3,5,7,4]])
        for i in range(28):
            A[pos[0,i],pos[1,i]]=1
            
    elif(symmetry==5):
        pos=np.array([[0,0,0,0,0,1,2,2,2,3,3,3,3,4,4,5,5,5,5,6,6,6,7,8,8,8,8,8],[0,2,3,7,8,0,4,5,8,2,3,5,8,2,6,0,3,5,6,0,3,4,8,0,1,5,6,8]])
        for i in range(28):
            A[pos[0,i],pos[1,i]]=1
    
    elif(symmetry==6):
        pos=np.array([[0,0,1,1,1,1,1,2,2,2,2,3,3,3,5,5,5,6,6,6,6,7,7,7,7,7,8,8],[1,5,1,2,5,7,8,2,5,6,7,0,1,2,6,7,8,1,2,3,6,0,1,3,6,7,3,7]])
        for i in range(28):
            A[pos[0,i],pos[1,i]]=1
            
    elif(symmetry==7):
        pos=np.array([[0,0,0,1,1,1,2,2,2,3,3,3,4,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8],[0,5,8,1,4,7,3,4,5,0,2,6,1,2,6,7,2,6,8,3,4,5,1,4,7,0,3,8]])
        for i in range(28):
            A[pos[0,i],pos[1,i]]=1
            
    elif(symmetry==8):
        pos=np.array([[0,1,1,1,1,2,2,2,2,3,3,3,3,3,5,5,5,5,5,6,6,6,6,7,7,7,7,8],[1,0,1,2,7,0,1,4,5,0,1,4,5,6,2,3,4,7,8,3,4,7,8,1,6,7,8,7]])
        for i in range(28):
            A[pos[0,i],pos[1,i]]=1
            
    elif(symmetry==9):
        pos=np.array([[0,0,0,1,1,1,1,1,2,3,3,3,3,4,4,5,5,5,5,6,7,7,7,7,7,8,8,8],[1,2,6,0,1,2,3,5,3,1,3,7,8,2,6,0,1,5,7,5,3,5,6,7,8,2,6,7]])
        for i in range(28):
            A[pos[0,i],pos[1,i]]=1
            
    elif(symmetry==10):
        pos=np.array([[0,1,1,1,1,1,2,2,2,3,3,4,4,4,4,5,5,6,6,6,7,7,7,7,7,8],[6,3,4,5,6,7,3,6,8,2,8,0,1,7,8,0,6,0,2,5,1,2,3,4,5,2]])
        for i in range(26):
            A[pos[0,i],pos[1,i]]=1
            
    elif(symmetry==11):
        pos=np.array([[0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8],[2,3,2,3,6,1,7,8,4,7,8,3,4,5,0,1,4,0,1,7,2,5,6,5,6]])
        for i in range(25):
            A[pos[0,i],pos[1,i]]=1
            
    elif(symmetry==12):   #very slow to find prob with this sym pattern
        pos=np.array([[0,1,1,1,1,2,2,2,2,3,3,3,4,5,5,5,6,6,6,6,7,7,7,7,8],[5,2,3,5,6,1,2,6,7,0,1,7,4,1,7,8,1,2,6,7,2,3,5,6,3]])
        for i in range(25):
            A[pos[0,i],pos[1,i]]=1
            
    elif(symmetry==13):   #very slow to find prob with this sym pattern
        pos=np.array([[0,1,1,1,1,2,2,3,3,3,4,4,4,5,5,5,6,6,7,7,7,7,8],[1,0,2,3,7,3,4,1,7,8,0,4,8,0,1,7,4,5,1,5,6,8,7]])
        for i in range(23):
            A[pos[0,i],pos[1,i]]=1
            
    elif(symmetry==14):     #very slow to find prob with this sym pattern
        pos=np.array([[0,0,0,0,1,1,1,1,3,3,4,4,4,4,5,5,7,7,7,7,8,8,8,8],[3,4,7,8,3,4,7,8,0,1,0,1,7,8,7,8,0,1,4,5,0,1,4,5]])
        for i in range(24):
            A[pos[0,i],pos[1,i]]=1
            
    elif(symmetry==15):     #very slow to find prob with this sym pattern
        pos=np.array([[0,0,0,1,1,2,2,3,3,4,4,4,5,5,6,6,7,7,8,8,8],[1,4,7,0,8,2,6,3,5,0,4,8,3,5,2,6,0,8,1,4,7]])
        for i in range(21):
            A[pos[0,i],pos[1,i]]=1
            
    else:
        print("Given symmetry is wrong!")
        A=makeNewSudo(np.zeros((9,9), dtype=int),1)
        
    return A









    
    
    
