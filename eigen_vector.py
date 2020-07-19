import eigen_value
import rank
import numpy as np
from numpy import linalg as LA

# Assuming Ax=b assuming full rank matrix (or determinant of matrix>0)
def swapRow(matrix, i, j):
    temp = matrix[i]
    matrix[i] = matrix[j]
    matrix[j] = temp
    return 

def nonZero(a):
    return a!=0

def reduction(matrix, i_base , j):
    multiplier = matrix[j][i_base]/matrix[i_base][i_base]

    for i in range(len(matrix[0])):
        matrix[j][i] = matrix[j][i] - multiplier*matrix[i_base][i]
    return

def elimination(matrix):
    row= len(matrix)
    
    i =0
    while(i<row):
        if nonZero(matrix[i][i]):
            for j in range(i+1,row):
                reduction(matrix, i, j)
        else:
            swap = False
            for k in range(i+1, row):
                if nonZero(matrix[k][i]):
                    swapRow(matrix, k, i)
                    
                    swap = True
                    i = i - 1
                    break
        i = i + 1
    
    return matrix

def get_dot(vector1, vector2, index):
    sol = 0
    for i in range(len(vector1)):
        if i!=index:
            sol = sol + (vector1[i]*vector2[i])
    return sol

def get_soln(matrix):
    vector = [0]*len(matrix)
    _rank = rank.rankOfMatrix(matrix)

    for i in range(len(matrix)-1,_rank-1,-1):
        vector[i] =1.0

    for i in range(_rank-1,-1,-1):
        b = matrix[i][-1]
        rest =  matrix[i][:-1]

        c = get_dot(vector,rest, i)
        x = (b-c)/rest[i] if rest[i]!=0 else 0
        vector[i] = x

    return vector

def _round(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = round(matrix[i][j],4)
    return 

def solve(A,b):
    for i in range(len(b)):
        A[i].append(b[i])
    
    matrix = elimination(A)
    _round(matrix)
    
    return get_soln(matrix)

def eigen_vector(A):
    # Ax = bx, where b is eigen value
    eigen_values = eigen_value.iterate(A)

    sol =[]
    A = np.array(A)
    b = [0]*len(A[0])
    
    for val in eigen_values:
        identity = np.identity(len(A))
        matrix = A - val*identity
        matrix = matrix.tolist()
        sol.append(solve(matrix,b))
    
    return sol

matrix = [[1,2,10],[1,4,5],[0,3,6]]
print(eigen_vector(matrix))
