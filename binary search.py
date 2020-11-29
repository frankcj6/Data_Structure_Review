#  linear search
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False


#  binary search
def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target > data[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False


def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target > data[mid]:
            return binary_search_recursive(data, target, mid + 1, high)
        else:
            return binary_search_recursive(data, target, low, mid - 1)


data = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]
target = 11
print(binary_search_recursive(data, target, 0, len(data) - 1))
print(binary_search_iterative(data, target))


#  find closest number
def closest_number(data, target):
    min_diff = float('inf')
    low = 0
    high = len(data) - 1
    closest_num = None
    if len(data) == 0:
        return None
    if len(data) == 1:
        return data[0]
    while low <= high:
        mid = (low + high) // 2
        if mid + 1 < len(data):
            min_dff_right = abs(data[mid + 1] - target)
        if mid > 0:
            min_dff_left = abs(data[mid - 1] - target)
        if min_dff_left < min_dff_right:
            min_diff = min_dff_left
            closest_num = data[mid - 1]
        if min_dff_right < min_dff_left:
            min_diff = min_dff_left
            closest_num = data[mid + 1]
        if data[mid] < target:
            low = mid + 1
        elif data[mid] > target:
            high = mid - 1
        else:
            return data[mid]
    return closest_num


s = [1, 2, 3, 6, 7, 8, 11]
print(closest_number(s, 9))


#  find fixed point at a distinct sorted array

def fixed_point(s1):
    low = 0
    high = len(s1) - 1

    while low <= high:
        mid = (low + high) // 2
        if s1[mid] < mid:
            low = mid + 1
        elif s1[mid] > mid:
            high = mid - 1
        elif s1[mid] == mid:
            return s1[mid]
    return None


s2 = [-1, 1, 3, 4, 5]
print(fixed_point(s2))

#  find bitonic peak
def find_highest_number(A):
    low = 0
    high = len(A)-1
    if len(A) < 3:
        return None
    while low<= high:
        mid = (low + high)//2
        mid_left = A[mid-1] if mid > 1 else float('-inf')
        mid_right = A[mid+1] if mid +1 < len(A) else float('-inf')
        if mid_left< A[mid] and A[mid] < mid_right:
            low = mid + 1
        elif mid_left > A[mid] and A[mid] > mid_right:
            high = mid -1
        elif mid_left < A[mid] and A[mid] > mid_right:
            return A[mid]

A = [1,2,3,4,3,2,1]
print(find_highest_number(A))

import bisect
#  bisect method
#  built-in version of python
A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
print(bisect.bisect_left(A, -10))

#  first occurence of 285
print(bisect.bisect_left(A, 285))

#  index after element
print(bisect.bisect_right(A, 285))

#  insert number in a certain order
bisect.insort_left(A, -10)
print(A)

#  integer square root
k = 300
def integer_square_root(k):
    low = 0
    high = k
    while low <= high:
        mid = (low+high)//2
        if mid*mid <= k:
            low = mid + 1
        else:
            high = mid - 1
    return low - 1

print(integer_square_root(300))


#  cyclical sorted list
A = [4, 5, 6, 7, 1, 2, 3]


def find_cyclical_list(A_):
    low = 0
    high = len(A_)-1
    while low < high:
        mid = (low + high)//2
        if A_[mid] > A_[high]:
            low = mid + 1
        elif A_[mid] <= A_[high]:
            high = mid
    return low

print(find_cyclical_list(A))
