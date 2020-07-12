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

def rankOfMatrix(matrix):
    row, col = len(matrix), len(matrix[0])

    count = min(col,row)

    i =0
    while(i<row):
        if nonZero(matrix[i][i]):
            for j in range(min(col,row)):
                if j!=i:
                    reduction(matrix, i, j)
        else:
            swap = False
            for k in range(i+1, row):
                if nonZero(matrix[k][i]):
                    swapRow(matrix, k, i)
                    swap = True
                    i = i - 1
                    break
            if (not swap):
                count -=1
        i = i + 1
    return count

matrix = [[1,2,3,5],[1,2,3,5],[10,16,17,19],[10,23,17,19]]

print("Rank of given matrix is {}".format(rankOfMatrix(matrix)))
