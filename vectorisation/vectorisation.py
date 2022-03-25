"""
A simple python module to give an example of how code can be vectorised.

"""
import numpy as np
import timeit

def a_slow_function(n=100,scale=0.4):

    if scale > 1:
        total = 0
        for i in range(1,n+1):
            total += scale*i
    else:
        total = 1
        for i in range(1,n+1):
            total *= (scale - i)
    return total


def a_vectorised_function(n=100,scale=0.4):

    array = np.arange(1,n+1)
    if scale > 1:
        total = scale * sum(array)
    else:
        total = np.prod(scale - array)
        
    return total
