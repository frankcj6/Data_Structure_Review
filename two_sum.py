def two_sum(nums, target):
    if not nums:
        return None
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]
    return None


def two_sum_2(nums, target):
    if not nums:
        return None
    dic = {}
    for i in range(len(nums)):
        if (target - nums[i]) not in dic:
            dic[nums[i]] = i
        else:
            return [dic[target-nums[i]],i]
    return None
A = [3, 2, 4]
print(two_sum(A, 6))
print(two_sum_2(A, 6))
