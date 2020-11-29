def maj_ele(nums):
    nums.sort()
    count = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            count += 1
        else:
            count = 1
        if count > len(nums) // 2:
            return nums[i]


A = [3,2,3]
B = [2, 2, 1, 1, 1, 2, 2]
print(maj_ele(B))