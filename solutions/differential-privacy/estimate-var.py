# %load "../solutions/differential-privacy/estimate-var.py"

def var_1_estimator(p_1dp, n, p, k):
    """
    :param p_1dp: The estimates probability of our DP dataset.
    :param     n: The number of samples in our dataset.
    :param     p: The p value of our DP scheme.
    :param     k: The k value of our DP scheme.
    :    returns: An estimate of the variance of our DP dataset.
    """
    return p_1dp*(1-p_1dp)/(1-p)**2/n

var_1_hat = var_1_estimator(p_1dp, len(df), p, k)
var_1_hat