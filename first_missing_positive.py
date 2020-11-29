def first_positive(nums):
    n = len(nums)
    i = 0
    while i <n:
        while 1<= nums[i]<= n:
            idx = nums[i]-1
            if nums[i] == nums[idx]:
                break
            nums[i], nums[idx] = nums[idx], nums[i]
        i += 1
    for i in range(n):
        if nums[i]!= i+1:
            return i+1
    return n+1


A = [3,4,-1,1]
print(first_positive(A))