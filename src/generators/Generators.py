import numpy as np
from copy import deepcopy
import time
from src.utils import SolverUtils as SV
from src.utils import GeneratorUtils as GU
from src.checkers import SudoCheck as SC
from src.solver import solver as SL
from random import randint


def GenerateProb(lb,ub,sym):
    if sym>0:
        return GenSymmetrical(sym)
    Known = randint(lb,ub)
    
    while(True):
        A= RandGeneratorTimLim([],Known,1,[],0)
        if (A[0][0]!=-1):
	        return A
    #return RandGenerator3([],Known,1,[])    #no time limit


def RandGenerator(A,Known,n):    #Top-down - No simulated annealing
    Arec=deepcopy(A)
    if (n==1):
        Arec=GU.makeNewSudo(np.zeros((9,9), dtype=int),1)
        return RandGenerator(Arec,Known,2)
    else:
        print(Arec)
        pos2erase=np.array(np.where(Arec!=0))
        lenPos=pos2erase[0,:].size
        print(lenPos)
        if (lenPos==Known):
            return Arec
        while (lenPos>0):
            A3=deepcopy(Arec)
            pick=randint(0, lenPos-1)
            A3[pos2erase[0,pick],pos2erase[1,pick]]=0
            if (GU.CountSolutions(A3,[],0,1)==1):
                A2=RandGenerator(A3,Known,2)
                lenKn=np.array(np.where(A2!=0))
                if(lenKn[0,:].size==Known):
                    return A2
            pos2erase=np.delete(pos2erase,pick,1)
            lenPos=pos2erase[0,:].size
        return Arec


def RandGeneratorTimLim(A,Known,n,Abeg,tim):   #Top-dowm, simulated annealing with time limit
    Arec=deepcopy(A)
    start2=time.time()
    if (n==1):
        Arec=GU.makeNewSudo(np.zeros((9,9), dtype=int),1)
        start=time.time()
        return RandGeneratorTimLim(Arec,Known,2,Arec,0)
    else:
        if (time.time()-start2+tim>15):
            #print("time limit exceed: ", time.time()-start2+tim)
            Arec[0][0]=-1
            return Arec
        pos2erase=np.array(np.where(Arec!=0))
        lenPos=pos2erase[0,:].size
        if (lenPos==Known):
            return Arec
        if (lenPos<27):
            p=(lenPos)/(81*2)
            x=np.random.uniform(0.0,1.0)
            if (x<=p):
                for i in range(2):
                    pos2fill=np.array(np.where(Arec==0))
                    lenFill=pos2fill[0,:].size
                    pick=randint(0, lenFill-1)
                    Arec[pos2fill[0,pick],pos2fill[1,pick]]=Abeg[pos2fill[0,pick],pos2fill[1,pick]]
                pos2erase=np.array(np.where(Arec!=0))
                lenPos=pos2erase[0,:].size
        while (lenPos>0):
            A3=deepcopy(Arec)
            pick=randint(0, lenPos-1)
            A3[pos2erase[0,pick],pos2erase[1,pick]]=0
            if (GU.CountSolutions(A3,[],0,1)==1):
                A2=RandGeneratorTimLim(A3,Known,2,Abeg,time.time()-start2+tim)
                if (A2[0][0]==-1):
                    return A2
                lenKn=np.array(np.where(A2!=0))
                if(lenKn[0,:].size==Known):
                    return A2
            pos2erase=np.delete(pos2erase,pick,1)
            lenPos=pos2erase[0,:].size
        return Arec


def RandGenerator3(A,Known,n,Abeg):   #Top-down with Simulated Annealing no time limit
    Arec=deepcopy(A)
    if (n==1):
        Arec=GU.makeNewSudo(np.zeros((9,9), dtype=int),1)
        return RandGenerator3(Arec,Known,2,Arec)
    else:
        pos2erase=np.array(np.where(Arec!=0))
        lenPos=pos2erase[0,:].size
        if (lenPos==Known):
            return Arec
        if (lenPos<27):
            p=(lenPos)/(81*2)
            x=np.random.uniform(0.0,1.0)
            if (x<=p):
                for i in range(2):
                    pos2fill=np.array(np.where(Arec==0))
                    lenFill=pos2fill[0,:].size
                    pick=randint(0, lenFill-1)
                    Arec[pos2fill[0,pick],pos2fill[1,pick]]=Abeg[pos2fill[0,pick],pos2fill[1,pick]]
                pos2erase=np.array(np.where(Arec!=0))
                lenPos=pos2erase[0,:].size
        while (lenPos>0):
            A3=deepcopy(Arec)
            pick=randint(0, lenPos-1)
            A3[pos2erase[0,pick],pos2erase[1,pick]]=0
            if (GU.CountSolutions(A3,[],0,1)==1):
                A2=RandGenerator3(A3,Known,2,Abeg)
                lenKn=np.array(np.where(A2!=0))
                if(lenKn[0,:].size==Known):
                    return A2
            pos2erase=np.delete(pos2erase,pick,1)
            lenPos=pos2erase[0,:].size
        return Arec


def RandFillGen(A,Known,n,Abeg):    #Bottom-up
    Arec=deepcopy(A)
    if (n==1):
        Arec=GU.makeNewSudo(np.zeros((9,9), dtype=int),1)
        return RandFillGen(np.zeros((9,9), dtype=int),Known,2,Arec)
    recKnown=np.array(np.where(Arec!=0))
    lenKnown=recKnown[0,:].size
    pos2fill=np.array(np.where(Arec==0))
    lenFill=pos2fill[0,:].size
    if (lenKnown >Known-2):
        p=7*(1/lenKnown)
        x=np.random.uniform(0.0,1.0)
        if (x<=p):
                print("done")
                for i in range(4):
                    pos2erase=np.array(np.where(Arec!=0))
                    lenPos=pos2erase[0,:].size
                    pick=randint(0, lenPos-1)
                    Arec[pos2erase[0,pick],pos2erase[1,pick]]=0
                pos2fill=np.array(np.where(Arec==0))
                lenFill=pos2fill[0,:].size
                recKnown=np.array(np.where(Arec!=0))
                lenKnown=recKnown[0,:].size
    if (lenKnown<Known-1):
        while (lenFill>0):
            A2=deepcopy(Arec)
            pick=randint(0, lenFill-1)
            A2[pos2fill[0,pick],pos2fill[1,pick]]=Abeg[pos2fill[0,pick],pos2fill[1,pick]]
            pos2fill=np.delete(pos2fill,pick,1)
            lenFill=pos2fill[0,:].size
            A3=RandFillGen(A2,Known,2,Abeg)
            recKnown=np.array(np.where(A3!=0))
            lenKnown=recKnown[0,:].size
            if (lenKnown==Known):
                return A3
        return Arec
    else:
        
        while (lenFill>0):
            print("edw",lenKnown)
            A2=deepcopy(Arec)
            pick=randint(0, lenFill-1)
            A2[pos2fill[0,pick],pos2fill[1,pick]]=Abeg[pos2fill[0,pick],pos2fill[1,pick]]
            if (GU.CountSolutions(A2,[],0,1)==1):
                print("in")
                print(A2)
                return A2
            print("out")
            A2[pos2fill[0,pick],pos2fill[1,pick]]=0
            print(A2)
            recKnown=np.array(np.where(A2!=0))
            lenKnown=recKnown[0,:].size
            pos2fill=np.delete(pos2fill,pick,1)
            lenFill=pos2fill[0,:].size
        return Arec
    
    
def GenSymmetrical(symmetry):
    A=GU.giveSymMat(symmetry)
    while (True):
        B=GU.makeNewSudo(np.zeros((9,9), dtype=int),1)
        for i in range(9):
            for j in range(9):
                if (A[i,j]!=0):
                    A[i,j]=B[i,j]
        if (GU.CountSolutions(A,[],0,1)==1):
            return A
    
