def set_zero(matrix):
    m = len(matrix)
    n = len(matrix[0])
    row_dic = []
    col_dic = []
    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 0:
                row_dic.append(row)
                col_dic.append(col)
    for row in row_dic:
        for col in range(n):
            matrix[row][col]=0
    for row in range(m):
        for col in col_dic:
            matrix[row][col] = 0
    return matrix

#  constant space o(1)
def set_zero_2(matrix):
    m = len(matrix)
    n = len(matrix[0])

    for row in range(m):
        for col in range(n):
            if matrix[row][col]==0:
                for row_idx in range(m):
                    if matrix[row_idx][col]!=0:
                        matrix[row_idx][col] = '2'
                for col_idx in range(n):
                    if matrix[row][col_idx]!=0:
                        matrix[row][col_idx]='2'

    for row in range(m):
        for col in range(n):
            if matrix[row][col] == '2':
                matrix[row][col]=0
    return matrix






matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(set_zero(matrix))
matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(set_zero_2(matrix))