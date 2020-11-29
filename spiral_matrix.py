def spiral_matrix(matrix):
    if not matrix or not matrix[0]:
        return []
    cur_row, cur_col = -1,-1
    output = []
    m = len(matrix)
    n = len(matrix[0])
    while m>1 and n>1:
        cur_row += 1
        cur_col += 1
        for k in range(n-1):
            output.append(matrix[cur_row][cur_col])
            cur_col += 1
        for k in range(m-1):
            output.append(matrix[cur_row][cur_col])
            cur_row += 1
        for k in range(n-1):
            output.append(matrix[cur_row][cur_col])
            cur_col -= 1
        for k in range(m-1):
            output.append(matrix[cur_row][cur_col])
            cur_row -= 1
        m -= 2
        n -= 2
    cur_row += 1
    cur_col += 1
    if n == 1:
        for k in range(m):
            output.append(matrix[cur_row][cur_col])
            cur_row += 1
    elif m == 1:
        for k in range(n):
            output.append(matrix[cur_row][cur_col])
            cur_col += 1
    return output

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiral_matrix(matrix))