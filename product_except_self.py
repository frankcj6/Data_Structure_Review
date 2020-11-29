def product_except_self(nums1):
    left = [1]*len(nums1)
    right = [1]*len(nums1)
    res = [0]* len(nums1)
    for i in range(1, len(nums1)):
        left[i] = left[i-1]*nums1[i-1]
    for i in range(len(nums1)-2, -1, -1):
        right[i] = right[i+1]*nums1[i+1]
    for i in range(len(nums1)):
        res[i] = left[i]*right[i]
    return res



def product_except_self_2(nums1):
    res = [1]*len(nums1)
    for i in range(1, len(nums1)):
        res[i] = res[i-1]*nums1[i-1]
    R = 1
    for i in range(len(nums1)-1, -1, -1):
        res[i]*= R
        R*= nums1[i]
    return res

nums1 = [1, 2, 3, 4]
print(product_except_self(nums1))
print(product_except_self_2(nums1))