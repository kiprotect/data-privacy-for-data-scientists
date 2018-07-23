import numpy as np

def epsilon(p, k):
    return -np.log(1-p*(1-k))
