def mysqrt(x):
    low = 0
    high = x
    res = 0
    while low <= high:
        mid = (low + high)//2
        if mid*mid <= x:
            res = mid
            low = mid + 1
        else:
            high = mid -1
    return res



