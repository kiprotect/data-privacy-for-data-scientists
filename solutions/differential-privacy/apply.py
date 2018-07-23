# %load "../solutions/differential-privacy/apply.py"

import numpy as np

p = 0.5
k = 0.5

values = []
df['income_binary'] = np.where(df['income'] == '<=50k', 0, 1)
df['income_dp'] = 0
for i, x in enumerate(df['income_binary']):
    values.append (process_value(x, p, k))

df['income_dp'] = np.array(values)
df['income_dp'][:10]
