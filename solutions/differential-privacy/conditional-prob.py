def p_cond(p, k, p_1):
    """
    :param   p: The probability of returning a random value instead of the true one
    :param   k: The probability of returning 1 when generating a random value
    :param p_1: The probability of a person to have an attribute value x_i=1
    """
    return (1-p*k)*p_1/((1-p)*p_1+p*(1-k))