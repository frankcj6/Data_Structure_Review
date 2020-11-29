def unique_path(m, n):
    dp = [[1 for j in range(n)] for i in range(m)]
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]

print(unique_path(3,7))