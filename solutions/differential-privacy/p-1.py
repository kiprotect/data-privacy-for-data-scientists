# %load "../solutions/differential-privacy/p-1.py"
def p_1_estimator(p_1dp, p, k):
    """
    :param p_1dp: The empirical probability of x_i=1 of our DP dataset.
    :param     p: The p value of our DP scheme.
    :param     k: The k value of our DP scheme.
    :    returns: An estimate of p_1 of our DP dataset.
    """
    return (p_1dp-p*(1-k))/(1-p)