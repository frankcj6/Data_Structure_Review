#  Two Sum Solution for leetcode
A1 = [-2, 1, 2, 4, 7, 11]
target1 = 13


#  Solution 1: Bruce Force
#  Time Complexity: O(n^2)
#  Space Complexity: O(1)

def two_sum_brute_force(A, target):
    if not A:
        return False
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            if A[i] + A[j] == target:
                print(A[i], A[j])
                return True
    return False


print(two_sum_brute_force(A1, target1))


#  Solution 2: Hash Table Two Sum
#  Time Complexity: O(n)
#  Space Complexity: O(n)


def two_sum_hash(A, target):
    if not A:
        return False
    HT = dict()
    for i in range(len(A)):
        if A[i] in HT:
            print(HT[A[i]], A[i])
            return True
        else:
            HT[target - A[i]] = A[i]
    return False


print(two_sum_hash(A1, target1))


#  Solution 3: Two pointer two sum
#  Time Complexity: O(n)
#  Space Complexity: O(1)


def Two_Pointer_two_sum(A, target):
    if not A:
        return False
    i = 0
    j = len(A) - 1
    while i <= j:
        if A[i] + A[j] == target:
            print(A[i], A[j])
            return True
        elif A[i] + A[j] < target:
            i += 1
        else:
            j -= 1
    return False


print(Two_Pointer_two_sum(A1, target1))
