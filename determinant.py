
def cofactor(matrix, row, col):
    sol = []
    for i in range(len(matrix)):
        vector = []
        for j in range(len(matrix)):
            if (i!=row and j != col):
                vector.append(matrix[i][j])

        if (len(vector)):
            sol.append(vector)
    return sol

def determinant(matrix):

    if len(matrix) ==1:
        return matrix[0][0]
    
    sol =0
    for i in range(len(matrix)):
        new_matrix = cofactor(matrix, 0, i)
        if(i%2==0):
            sol = sol + matrix[0][i]*determinant(new_matrix)
        else:
            sol = sol - matrix[0][i]*determinant(new_matrix)

    return sol

matrix = [[1,2,3,5],[1,2,3,9],[10,16,17,19],[10,23,17,19]]

print("Determinant of the above matrix {}".format(determinant(matrix)))