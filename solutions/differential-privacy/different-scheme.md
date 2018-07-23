Let's consider the two cases when a person's true value is 0 and 1, respectively:

* If the value is 0, the database state will remain unchanged with certainty,
  hence the epsilon is 0.
* If the value is 1, the database state will remain unchanged with probability
  $p$, hence $\epsilon=-\ln{p}$.

Hence, the epsilon of the scheme is $\epsilon = - \ln{p}$.