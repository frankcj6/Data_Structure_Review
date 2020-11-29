def max_sub(nums):
    max_sum = float('-inf')
    cur = 0
    for i in range(len(nums)):
        cur = max(cur+nums[i], nums[i])
        max_sum = max(cur, max_sum)
    return max_sum

A = [-1,3,4,-4,-3]
print(max_sub(A)