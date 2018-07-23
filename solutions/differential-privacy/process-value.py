def process_value(value, p, k):
    """
    :param value: The value to apply the differentially private scheme to.
    :param     p: The probability of returning a random value instead of the true one
    :param     k: The probability of returning 1 when generating a random value
    :    returns: A new, differentially private value
    """