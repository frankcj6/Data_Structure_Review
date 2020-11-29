def first_last(nums, target):
    low_1 = 0
    high_1 = len(nums)-1
    low_bound = -1
    while low_1<= high_1:
        mid_1 = (low_1+high_1)//2
        if target <= nums[mid_1]:
            if target == nums[mid_1]:
                low_bound = mid_1
            high_1 = mid_1 -1
        else:
            low_1 = mid_1 + 1

    low_2 = 0
    high_2 = len(nums)-1
    high_bound = -1
    while low_2<= high_2:
        mid_2 = (low_2+high_2)//2
        if target >= nums[mid_2]:
            if target == nums[mid_2]:
                high_bound = mid_2
            low_2 = mid_2 +1
        else:
            high_2 = mid_2 -1
    return [low_bound, high_bound]


A = [5, 7, 7, 8, 8, 10]
print(first_last(A, 8))