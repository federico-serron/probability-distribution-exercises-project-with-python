# P(y=1) = 0.2
# P(y=0) = 0.8

import numpy as np
from scipy.stats import binom

def dbinom(x,size,prob=0.5):
    """
    Calculates the point estimate of the binomial distribution
    """
    result=binom.pmf(k=x,n=size,p=prob,loc=0)
    return result

def pbinom(q,size,prob=0.5):
    """
    Calculates the cumulative of the binomial distribution
    """
    from scipy.stats import binom
    result=binom.cdf(k=q,n=size,p=prob,loc=0)
    return result


x = dbinom(2, 100, 0.2)

# P(y <= 10) = P(y=0)+P(y=1)...+P(y=10)
y = pbinom(10, 100, 0.2)
print(y*100)

# Dado de 4 caras azules (B) y dos rojas (R)
# R,B,R,R,R
# R,B,R,R,R,B
# B,R,R,R,R,R

