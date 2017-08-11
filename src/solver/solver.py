from copy import deepcopy
import numpy as np
from src.utils import SolverUtils as SV
from src.checkers import SudoCheck as SC


def SudoSolveIt(A,C,n):
    if n==1:
        C=SV.ConstructC(A)
        return SudoSolveIt(A,C,2)
    else:
        if np.min(A)>0:
            return A
        C, t2 = SV.SwordFishEr(C)
        if(t2):
            print("done")
        A, C, DidIn = SV.SudoInput1(A,C)
        A, C, DidIn = SV.SudoInput2(A,C)
        C, t2 = SV.SwordFishEr(C)
        #C, t = SV.XWingEr(C)
        #print(C)
        
        C, t = SV.CandLineEr(C)
        #C, t = SV.XWingEr(C)
        C, t = SV.multLineEr(C)
        #C, t2 = SV.SwordFishEr(C)
        #C, t = SV.nakedPairEr(C)
        #C, t = SV.nakedTuplesEr(C)
        C, t = SV.hiddenPairEr(C)
        #C, t = SV.hiddenTupleEr(C)
        #C, t2 = SV.SwordFishEr(C)
        
        if(t2):
            print("done")
        
        return SudoSolveIt(A,C,2)


def SudoSolveIt1(A,C,n):
    Arec = deepcopy(A)
    Crec = deepcopy(C)
    if n==1:
        Crec=SV.ConstructC(Arec)
        return SudoSolveIt1(Arec,Crec,2)
    else:
        if (n==2):
            Arec, Crec, DidIn = SV.SudoInput1(Arec,Crec)
            return SudoSolveIt1(Arec,Crec,3)
        if np.min(Arec)>0:
            return Arec
        if (SC.IsDeadEnd(Crec)):
            return np.array([0,0])
        Arec, Crec, DidIn = SV.SudoInput1(Arec,Crec)
        if (DidIn):
            return SudoSolveIt1(Arec,Crec,3)
        else:
            r=SV.FindMinRow(Crec)
            rC=Crec[r,:]
            for i in range(9):
                if (rC[i]>0):
                    A2=deepcopy(Arec)
                    C2=deepcopy(Crec)
                    A2[rC[9],rC[10]]=rC[i]
                    C2=SV.clearC(C2,rC[9],rC[10],rC[11],rC[i])
                    C2=np.delete(C2,r,0)
                    A2=SudoSolveIt1(A2,C2,3)
                    if np.min(A2)>0:
                        return A2
            return A2


def SudoSolveIt2(A,C,n):    #Fastest Solver
    Arec = A
    Crec = C
    if n==1:
        Crec=SV.ConstructC(Arec)
        return SudoSolveIt2(Arec,Crec,2)
    else:
        if (n==2):
            Arec, Crec, DidIn = SV.SudoInput1(Arec,Crec)
            Arec, Crec, DidIn = SV.SudoInput2(Arec,Crec)
            return SudoSolveIt2(Arec,Crec,3)
        if np.min(Arec)>0:
            return Arec
        if (SC.IsDeadEnd(Crec)):
            return np.array([0,0])
        Arec, Crec, DidIn = SV.SudoInput1(Arec,Crec)
        if (DidIn):
            if (SC.IsDeadEnd(Crec)):
                return np.array([0,0])
            else:
                Arec, Crec, DidIn = SV.SudoInput2(Arec,Crec)
                return SudoSolveIt2(Arec,Crec,3)
        else:
            Arec, Crec, DidIn = SV.SudoInput2(Arec,Crec)
            if (DidIn):
                return SudoSolveIt2(Arec,Crec,3)
        r=SV.FindMinRow(Crec)
        rC=Crec[r,:]
        for i in range(9):
            if (rC[i]>0):
                A2=deepcopy(Arec)
                C2=deepcopy(Crec)
                A2[rC[9],rC[10]]=rC[i]
                C2=SV.clearC(C2,rC[9],rC[10],rC[11],rC[i])
                C2=np.delete(C2,r,0)
                A2=SudoSolveIt2(A2,C2,3)
                if np.min(A2)>0:
                    return A2
        return A2


def SudoBruteSolve(A,n):    #Brute Force solver
    if (SC.IsSudoRight(A)):
        return A
    Arec=deepcopy(A)
    for i in range(9):
        for j in range(9):
            if (Arec[i,j]==0):
                posnum=SV.FindPosNums(Arec,i,j)
                if (posnum.size>0):
                    for k in range(posnum.size):
                        Arec[i,j]=posnum[k]
                        A2=SudoBruteSolve(Arec,n)
                        if (SC.IsSudoRight(A2)):
                            return A2
                    return A2
                else:
                    return Arec
                    
                

