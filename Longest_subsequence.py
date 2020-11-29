def length_longest_sub(nums):
    n = len(nums)
    if n<= 1:
        return n
    sub = [0]*n
    sub[0] = nums[0]
    size = 0
    for num in nums:
        l, r = 0, size -1
        while l<= r:
            mid = (l+r)//2
            if sub[mid]>= num:
                r= mid -1
            else:
                l = mid + 1
        sub[l] = num
        size = max(size, l+1)
    return size



#  dp solution
def length_sub(nums):
    if not nums:
        return 0
    n = [1]*len(nums)
    j = 1
    while j<len(nums)
        i = 0
        while i < j:
            if nums[i]<nums[j]:
                n[j] = max(n[j], n[i]+1)
            i += 1
        j += 1
    return max(n)


