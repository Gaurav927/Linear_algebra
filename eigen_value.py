from determinant_row_reduction import determinant
import gram_schmidt
import numpy as np
import determinant_row_reduction

EPSILON = 1e-4

def iterate(A):
    A = np.array(A)
    matrix = A.copy()

    for _ in range(20):
        Q = gram_schmidt.get_orthogonal(A)
        A = Q.T@A@Q
    
    pos_sol = [A[i][i] for i in range(A.shape[0])]
    sol = []
    for val in pos_sol:
        temp = matrix -val*np.identity(len(matrix))
        if abs(determinant_row_reduction.determinant(temp))<= EPSILON:
            sol.append(val)

    return sol

matrix = [[1,2,10],[1,4,5],[0,3,6]]

values = iterate(matrix)
print("Real eigen values of the above matrix is\n{}".format(values))
