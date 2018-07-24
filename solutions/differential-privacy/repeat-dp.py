p_1_hats = []

df['income_binary'] = np.where(df['income'] == '<=50k', 0, 1)
df['income_dp'] = 0

for j in range(500):

    values = []
    for i, x in enumerate(df['income_binary']):
        values.append (process_value(x, p, k))

    df['income_dp'] = np.array(values)
    p_1dp = df['income_dp'].sum()/len(df)
    p_1_hat = p_1_estimator(p_1dp, p, k)
    p_1_hats.append(p_1_hat)

p_1_hats = np.array(p_1_hats)