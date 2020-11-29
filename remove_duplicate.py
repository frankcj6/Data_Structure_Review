def remove_dup(nums):
    n = len(nums)
    i = 1
    while i< n:
        if nums[i] == nums[i-1]:
            nums.remove(nums[i])
            n -= 1
        else:
            i+= 1
    return nums

A = [0,0,1,1,1,2,3,4,5,6,6]
print(remove_dup(A))

