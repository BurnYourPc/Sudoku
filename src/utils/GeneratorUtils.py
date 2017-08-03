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


def makeNewSudo(A,n):
    Arec=deepcopy(A)
    if (np.min(Arec)>0):
        return Arec
    for i in range(9):
        for j in range(9):
            if (Arec[i,j]==0):
                posnum=SV.FindPosNums(Arec,i,j)
                #if (posnum.size>0)
                while (posnum.size>0):
                    pick=randint(0, posnum.size-1)
                    Arec[i,j]=posnum[pick]
                    A2=makeNewSudo(Arec,n+1)
                    if (np.min(A2)>0):
                        return A2
                    posnum=np.delete(posnum,pick)
                return Arec


#def getSudoPerm
