import numpy as np
import random

def process_value(value, p, k):
    """
    :param value: The value to apply the differentially private scheme to.
    :param     p: The probability of returning a random value instead of the true one
    :param     k: The probability of returning 1 when generating a random value
    :    returns: A new, differentially private value
    """
    rv = random.random()
    if rv <= p:
        #we return a random value
        rv = random.random()
        if rv <= k:
            return 0
        return 1
    else:
        return value

    
p = 0.5
k = 0.5
    
columns = ['no_primary_dr', 'has_diabetes']

for column in columns:
    binary_column = '{}_binary'.format(column)
    df[binary_column] = np.where(df[column] == False, 0, 1) 
    values = []
    for value in df[binary_column]:
        values.append(process_value(value, p, k))
    dp_column = '{}_dp'.format(column)
    df[dp_column] = np.array(values)
    
df[['no_primary_dr_binary','no_primary_dr_dp']][:20]
