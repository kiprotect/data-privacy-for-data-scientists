p_1 = df['income_binary'].sum()/len(df)
p_1dp = df['income_dp'].sum()/len(df)
print("True value: {:.3f}. DP-value: {:.3f}.".format(p_1, p_1dp))

p_1_hat = p_1_estimator(p_1dp, p, k)
print("Estimated true value: {:.3f}".format(p_1_hat))