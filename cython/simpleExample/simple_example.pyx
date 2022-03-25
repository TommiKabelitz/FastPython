import cython

# Optional compiler directives. Improve performance by removing checks.
# See cython documentation for more info.
# cython: boundscheck=False, wraparound=False, initalisedcheck=False

#Example function definition. This can be imported into python
cpdef long my_fun(int a,
                  float b,
                  str s,            
                  double[:] array): # This is the 'memoryview' syntax
                                    # Is the preferred array handling method

    # Note: For strings, recommended to avoid c-strings.
    # Just use the python string type as above

    cdef int i,j,k
    cdef double* array_pointer = &array[0]
    cdef int size = array.shape[0]
    cdef long return_val = 27
    c = c_fun(a)    # Note not typed as you do not have to type everything

    return return_val

# A function which cannot be imported into python
cdef int c_fun(int a):
    return 2*a
