import numpy as np
from copy import deepcopy
from src.utils import SolverUtils as SV
from src.utils import GeneratorUtils as GU
from src.checkers import SudoCheck as SC
from src.solver import solver as SL
from src.burnImage import burnSudo2Img as BS
from src.generators import Generators as Gen
from random import randint

B1=np.array([[1,4,0,0,0,0,0,0,0],[0,0,5,4,7,1,0,0,0],[0,0,7,5,0,0,0,0,9],[0,6,1,7,0,5,3,8,0],[0,7,8,1,0,3,6,9,0],[0,5,9,6,0,8,7,2,0],[5,0,0,0,0,7,2,0,0],[0,0,0,3,8,4,1,0,0],[0,0,0,0,0,0,0,3,7]])
B2=np.array([[0,0,0,0,9,0,7,0,8],[0,0,0,8,0,0,0,0,0],[5,1,0,6,0,7,0,0,0],[0,0,9,2,0,0,0,8,0],[6,0,0,0,0,0,0,0,4],[0,7,0,0,0,1,5,0,0],[0,0,0,5,0,9,0,6,1],[0,0,0,0,0,8,0,0,0],[2,0,3,0,7,0,0,0,0]])

# Solve B1,B2 with the fastest solver implemented
A1=SL.SudoSolveIt2(B1,[],1)
A2=SL.SudoSolveIt2(B2,[],1)

#Creating NonSymmetrical Problem with 23 known numbers
matrix=Gen.RandGenerator3([],23,1,[])
BS.CreateSudoImg(matrix,False)

#Creating Symmetrical Problems (symemetry is a naumber from 1 to 15, but 1-11 is efficient)
matrix=Gen.GenSymmetrical(5)
BS.CreateSudoImg(matrix,True)
matrix=Gen.GenSymmetrical(2)
BS.CreateSudoImg(matrix,True)
