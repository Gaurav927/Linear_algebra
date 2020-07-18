import math
import numpy as np

def normalize(vector):
    length = math.sqrt(sum([ele*ele for ele in vector]))
    return vector/length if length>0 else vector

def get_orthogonal(A):
    A = np.array(A)
    A = np.transpose(A)
    row = len(A)
    matrix = []
    matrix.append(normalize(A[0]))

    for i in range(1,row):
        temp = A[i]
        for j in range(i):
            temp = temp - np.dot(matrix[j],A[i])*matrix[j]
        matrix.append(normalize(temp))
        
    matrix = np.array(matrix)
    return np.transpose(matrix)

A =np.array([[1,2,4],[1,0,5],[0,3,6]])
print("Orthogonal basis of the above matrix \n{}".format(get_orthogonal(A)))
