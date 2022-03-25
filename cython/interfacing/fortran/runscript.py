"""
Simple script which runs a few iterations of Conway's game of life to demonstrate
interfacing python and fortran. updategrid is a cython function which interfaces
a fortran subroutine.
"""

#Import the function as if from a python module
from fortmod import updategrid

#For initialising array
import numpy as np
from random import randint

def main():
    #Grid size
    nx = 12
    ny = 12

    #Random array of 1s and 0s. Note that the datatype is the numpy equivalent of a
    #c int. python's int is double precision by default which can cause issues
    #Also note the order. This specifies fortran major memory layout, will cause seg
    #faults if missing.
    array = np.asarray([[randint(0,1) for i in range(1,nx+1)] for j in range(1,ny+1)],dtype=np.int32,order='F')

    #Running the game of life for 10 iterations
    print(array)
    print()
    for i in range(10):
        array = updategrid(array,nx,ny)
        print(np.asarray(array))
        print()

if __name__ == '__main__':

    main()
