def kthsmaller(matrix, k):
    n, m= len(matrix), len(matrix[0])
    def count_smaller(num):
        i, j, count = 0, m-1, 0
        while i<n and j>=0:
            if matrix[i][j]<num:
                count += j+1
                i += 1
            else:
                j -= 1
        return count
    def helper():
        low = matrix[0][0]
        high = matrix[-1][-1]
        while low<=high:
            mid = (low+high)//2
            if count_smaller(mid)>=k:
                high = mid -1
            else:
                low = mid +1
        return high
    return helper()
