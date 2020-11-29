def rotate(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]
    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))


def rotate_2(matrix):
    m = len(matrix[0])
    for i in range(m//2 + m%2):
        for j in range(m//2):
            tmp = matrix[m-1-j][i]
            matrix[m-1-j][i] = matrix[m-1-i][m-j-1]
            matrix[m-1-i][m-j-1] = matrix[j][m-1-i]
            matrix[j][m-1-i] = matrix[i][j]
            matrix[i][j] = tmp
    return matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate_2(matrix))