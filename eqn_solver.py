
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
    count = row
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
            if not swap:
                return "Dependent eqn found"
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

    for i in range(len(matrix)-1,-1,-1):
        b = matrix[i][-1]
        rest =  matrix[i][:-1]

        c = get_dot(vector,rest, i)
        x = (b-c)/rest[i]
        vector[i] = x

    return vector

def solve(A,b):
    for i in range(len(b)):
        A[i].append(b[i])
    
    matrix = elimination(A)
    return get_soln(matrix)

A = [[1,1,2],[-1,1,3],[0,0,-1]]
b =[1,1,1]

print("Solution of the above eqn Ax=b is {}".format(solve(A,b)))


