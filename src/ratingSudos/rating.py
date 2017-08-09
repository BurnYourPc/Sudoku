import numpy as np
from copy import deepcopy
from src.utils import RatingUtils as RU


def RateProb(A):
    Av=deepcopy(A)
    if (RU.isVeryEasy(Av)):
        return 1
    
    Av=deepcopy(A)
    if (RU.isEasy(Av)):
        return 2
        
    Av=deepcopy(A)
    if (RU.isMedium(Av)):
        return 3
    
    Av=deepcopy(A)
    if (RU.isHard(Av)):
        return 4
    
    Av=deepcopy(A)
    if (RU.isVeryHard(Av)):
        return 5
    
    return 6
