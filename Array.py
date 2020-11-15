def array_advance(A):
    if not A:
        return False

    furthest_reach = 0
    last_idx = len(A)-1
    i = 0
    while i <= furthest_reach and furthest_reach < last_idx:
        furthest_reach = max(furthest_reach, A[i]+i)
        i += 1

    return furthest_reach >= last_idx


#  implementation

A1 = [3, 3, 1, 0, 2, 0, 1]
A2 = [3, 2, 1, 0, 0, 0, 1]
A3 = []
print(array_advance(A1))
print(array_advance(A2))
print(array_advance(A3))


#  plus one algorithm
def plus_one_map(A):
    s = ''.join(map(str, A))
    s = int(s)+1
    return s


def plus_one_alg(A):
    if not A:
        return False
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A


A1 = [1, 4, 9]
B1 = [9, 9, 9]
print(plus_one_map(A1))
print(plus_one_map(B1))

print(plus_one_alg(A1))
print(plus_one_alg(B1))


