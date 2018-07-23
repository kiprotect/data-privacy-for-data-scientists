import numpy as np

def epsilon(p, k):
    """
    :param p: The probability of returning a random value instead of the true one
    :param k: The probability of returning 1 when generating a random value
    :returns: The epsilon for the given values of p, k
    """
    return -np.log(1-p*(1-k))
