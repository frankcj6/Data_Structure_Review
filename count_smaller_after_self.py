# brute force o(n^2)
def countsmaller(nums):
    res = []
    for i in range(len(nums)):
        count = 0
        for j in range(i+1, len(nums)):
            if nums[i]>nums[j]:
                count += 1

        res.append(count)
    return res

A = [5, 2, 6, 1]
print(countsmaller(A))

# binary search
def count_smaller_2(nums):
    t = []
    res = [0]*len(nums)
    for i in range(len(nums)-1, -1, -1):
        left = 0
        right = len(t)
        while left < right:
            mid = left + (right-left)//2
            if t[mid]>= nums[i]:
                right = mid
            else:
                left = mid + 1
        res[i] = right

        t.insert(right, nums[i])
    return res

print(count_smaller_2(A))
