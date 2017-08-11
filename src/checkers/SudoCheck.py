import numpy as np
from src.utils import SolverUtils as SU


def IsSudoRight(A):
    t=True
    if (np.min(A)==0):
        t=False
        return t
    for i in range(9):
        row=A[i,:]
        col=A[:,i]
        box = SU.get_matBox(i+1, A)
        if (np.unique(row).size<9):
            t=False
            break
        if (np.unique(col).size<9):
            t=False
            break
        if (np.unique(box).size<9):
            t=False
            break
    return t


def IsDeadEnd(C):    #Given C checks if no one cell could accept a value
    t=False
    nrows=C.shape
    nrows=nrows[0]
    for i in range(nrows):
        arr=C[i,0:9]
        if (arr[np.nonzero(arr)].size==0):
            t=True
            break
    return t
