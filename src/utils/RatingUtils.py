import numpy as np
from copy import deepcopy
from src.utils import SolverUtils as SV
from src.utils import GeneratorUtils as GU
from src.checkers import SudoCheck as SC
from src.solver import solver as SL
from src.burnImage import burnSudo2Img as BS
from src.generators import Generators as Gen



def isVeryEasy(A):
    C=SV.ConstructC(A)
    
    while (True):
        if np.min(A)>0:
            return True
        A, C, DidIn = SV.SudoInput2(A,C)
        if(not DidIn):
            return False


def isEasy(A):
    C=SV.ConstructC(A)
    
    while (True):
        if np.min(A)>0:
            return True
        A, C, DidIn2 = SV.SudoInput2(A,C)
        A, C, DidIn1 = SV.SudoInput1(A,C)
        if( (not DidIn1) and (not DidIn2) ):
            return False


def isMedium(A):
    C=SV.ConstructC(A)
    
    while (True):
        if np.min(A)>0:
            return True
        A, C, DidIn2 = SV.SudoInput2(A,C)
        A, C, DidIn1 = SV.SudoInput1(A,C)
        
        #--------medium-------#
        C, er3 = SV.CandLineEr(C)
        C, er4 = SV.multLineEr(C)
        if( (not DidIn1) and (not DidIn2) and (not er3) and (not er4) ):
            return False


def isHard(A):
    C=SV.ConstructC(A)
    
    while (True):
        if np.min(A)>0:
            return True
        A, C, DidIn2 = SV.SudoInput2(A,C)
        A, C, DidIn1 = SV.SudoInput1(A,C)
        C, er3 = SV.CandLineEr(C)
        C, er4 = SV.multLineEr(C)
        
        #------hard------#
        C, er5 = SV.nakedPairEr(C)
        C, er6 = SV.nakedTuplesEr(C)
        C, er7 = SV.hiddenPairEr(C)
        C, er8 = SV.hiddenTupleEr(C)
        if( (not DidIn1) and (not DidIn2) and (not er3) and (not er4) and (not er5) and (not er6) and (not er7) and (not er8) ):
            return False


def isVeryHard(A):
    C=SV.ConstructC(A)
    
    while (True):
        if np.min(A)>0:
            return True
        A, C, DidIn2 = SV.SudoInput2(A,C)
        A, C, DidIn1 = SV.SudoInput1(A,C)
        C, er3 = SV.CandLineEr(C)
        C, er4 = SV.multLineEr(C)
        C, er5 = SV.nakedPairEr(C)
        C, er6 = SV.nakedTuplesEr(C)
        C, er7 = SV.hiddenPairEr(C)
        C, er8 = SV.hiddenTupleEr(C)
        
        #---------very hard----------#
        C, er9 = SV.XWingEr(C)
        C, er10 = SV.SwordFishEr(C)
        if( (not DidIn1) and (not DidIn2) and (not er3) and (not er4) and (not er5) and (not er6) and (not er7) and (not er8) and (not er9) and (not er10) ):
            return False




