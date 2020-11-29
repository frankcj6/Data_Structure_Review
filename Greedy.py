#  greedy algorithm
#  pair the longest task with the shortest one
A = [6, 3, 2, 7, 5, 5]

def assign_greedy(A):
    A = sorted(A)
    for i in range(len(A)//2):
        print(A[i], A[-i])

print(assign_greedy(A))

