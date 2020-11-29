#  print all power subsets:
#  dfs

"""
                        []
                       /  \
                    [1]    [2]
                   /  \      \
                [1,2]  [1,3]  [2,3]
                /
            [1,2,3]
"""

def subsets(nums):
    res = []
    def dfs(nums, temp, i):
        res.append(temp[:])
        for i in range(i, len(nums)):
            temp.append(nums[i])
            dfs(nums, temp, i+1)
            temp.pop()
    dfs(nums, [], 0)
    return res



A = [1, 2, 3, 4]
print(subsets(A))