# http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.ndarray.html
# http://stackoverflow.com/questions/4151128/what-are-the-differences-between-numpy-arrays-and-matrices-which-one-should-i-u

import numpy as np


# Matrix
# Numpy matrices provide a convenient notation for matrix multiplication:
# if a and b are matrices, then a*b is their matrix product.
a=np.mat('4 3; '
         '2 1')


b=np.mat('1 2; '
         '3 4')

print(a*b)
# [[13 20]
#  [ 5  8]]

print a.I



c=np.array([[4, 3],
            [2, 1]])

d=np.array([[1, 2],
            [3, 4]])

print(c*d)
# [[4 6]
#  [6 4]]