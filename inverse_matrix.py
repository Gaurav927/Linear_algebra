
# Inverse using standard kramer's rule (exponential in running time)

def swapRow(matrix, i, j):
    temp = matrix[i]
    matrix[i] = matrix[j]
    matrix[j] = temp

    return 

def nonZero(a):
    return a!=0

def reduction(matrix,sol, i_base , j):
     
    multiplier = matrix[j][i_base]/matrix[i_base][i_base]

    for i in range(len(matrix[0])):
        matrix[j][i] = matrix[j][i] - multiplier*matrix[i_base][i]
        sol[j][i]    = sol[j][i] - multiplier*sol[i_base][i]
    return

def inverse(matrix):
    row= len(matrix)
    count = row
    sol = [[0]*row for _ in range(row)]
    for i in range(row):
        sol[i][i] =1

    i =0
    while(i<row):
        if nonZero(matrix[i][i]):
            for j in range(row):
                if(j!=i):
                    reduction(matrix,sol, i, j)
        else:
            swap = False
            for k in range(i+1, row):
                if nonZero(matrix[k][i]):
                    swapRow(matrix, k, i)
                    swapRow(sol,k,i)
                    swap = True
                    i = i - 1
                    break
            if not swap:
                return "Not invertible"
        i = i + 1
    
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            sol[i][j] = sol[i][j]/matrix[i][i]

    return sol


matrix = [[1,2,3,6],[1,2,5,10],[4,5,8,0],[3,6,7,9]]

print("Inverse of given matrix is {}".format(inverse(matrix)))



