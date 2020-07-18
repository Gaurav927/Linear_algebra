import gram_schmidt
import numpy as np
from numpy import linalg as LA

# use gram_schmidt function & the concept of similar matrix to calculate eigen values
def iterate(A):
    A = np.array(A)
    for _ in range(20):
        Q = gram_schmidt.get_orthogonal(A)
        A = Q.T@A@Q
        
    return [A[i][i] for i in range(A.shape[0])]

matrix = [[1,2,10],[0,0,5],[0,3,6]]
print(iterate(matrix))

    

