def jump_game(nums):
    max_idx = 0
    for i in range(len(nums)):
        if i <= max_idx:
            max_idx = max(max_idx, i+nums[i])
        else:
            return False
    return max_idx >= len(nums)-1

A = [2,3,1,1,4]
print(jump_game(A))


