def max_product_sub(nums):
    min_val = nums[0]
    max_val = nums[0]
    max_prod = nums[0]
    for i in range(1, len(nums)):
        max_val, min_val = max(nums[i], nums[i]*max_val, nums[i]*min_val), min(nums[i], nums[i]*min_val, nums[i]*max_val)
        max_prod = max(max_prod, max_val, min_val)
    return max_prod

A = [2,3,-2,4]
print(max_product_sub(A))


