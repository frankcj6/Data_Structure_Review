def find_duplicates(nums):
    stack = []
    for i in nums:
        if i not in stack:
            stack.append(i)
        else:
            return i

nums1 = [1,3,4,2,2]
print(find_duplicates(nums1))

def find_duplicates1(nums):
    nums.sort()
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = (low+high)//2
        if nums[mid] >= mid+1:
            low = mid +1
        if nums[mid]< mid+1:
            high = mid -1
    return nums[low]

nums1 = [1,3,4,2,2]
print(find_duplicates1(nums1))
