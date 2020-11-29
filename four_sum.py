def foursum(A, B, C, D):
    rec = {}
    N= len(A)
    for i in range(N):
        for j in range(N):
            sum2 = A[i]+B[j]
            if not sum2 in rec:
                rec[sum2] = 1
            else:
                rec[sum2] += 1
    res = 0
    for i in range(N):
        for j in range(N):
            sum2 = C[i] + D[j]
            if -sum2 in rec:
                res += rec[-sum2]
    return res
