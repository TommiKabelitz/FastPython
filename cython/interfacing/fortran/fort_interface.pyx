"""
Simple cython module which interfaces a fortran subroutine, allowing it to be called 
from within pure python.
"""

# First use extern to find function signature from header
cdef extern from "fort_interface.h":
    extern void c_updategrid(int* grid, int* nx, int* ny)

# cpdef to create a python interface to the function.
# int[:,:] is memoryview syntax. int[::1,:] specifies an integer
# array with fortran memory striding (columns are contiguous).
# This is essential for fortran functions to avoid segmentation
# faults. Also means incoming arrays must be column major. See the
# python runscript for an example showing this.
cpdef int[::1,:] updategrid(int[::1,:] grid, int nx, int ny):
    #Note that only a pointer to the first element of the array is
    #passed. Normal pointers are passed for other objects
    c_updategrid(&grid[0,0], &nx, &ny)

    return grid
