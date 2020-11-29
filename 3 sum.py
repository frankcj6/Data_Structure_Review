def three_sum(nums):
    nums.sort()
    i = 0
    j = len(nums) - 1
    result = []
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        target = 0 - nums[i]
        if i == 0 or nums[i] != nums[i - 1]:
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right += 1
                    left += 1
                    right -= 1
                elif s < target:
                    left += 1
                else:
                    right -= 1
    return result


#  Solution 2:  Binary Search
from bisect import bisect_right as bsr


def three_sum2(a):
    a.sort()
    result = []
    for i in range(len(a) - 2):
        if a[i] > 0:
            break
        if i > 0 and a[i] == a[i - 1]:
            continue
        l, r = i + 1, len(a) - 1
        while l < r:
            sum = a[i] + a[r] + a[l]
            if sum < 0:
                l += 1
            elif sum > 0:
                r -= 1
            else:
                result.append([a[i], a[l], a[r]])
                l = bsr(a, a[l])
    return result
