def matrix_scan(matrix, target):
    row = 0
    col = 0
    while row< len(matrix) and col<len(matrix[0]):
        left, right = col, len(matrix[0])-1
        while left<= right:
            mid = left+(right-left)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid -1
            else:
                left = mid +1
        top, bottom = row, len(matrix)-1
        while top<= bottom:
            mid2 = top+(bottom-top)//2
            if matrix[mid2][col] == target:
                return True
            elif matrix[mid2][col] > target:
                bottom = mid2 -1
            else:
                top = mid2 +1
        row += 1
        col += 1
    return False


