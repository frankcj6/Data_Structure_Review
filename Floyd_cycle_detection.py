def find_duplicate(nums):
    slow_pointer = nums[0]
    fast_pointer = nums[0]
    while(1):
        slow_pointer = nums[slow_pointer]
        fast_pointer = nums[nums[fast_pointer]]
        if slow_pointer == fast_pointer:
            break
    slow_pointer = nums[0]
    while slow_pointer != fast_pointer:
        slow_pointer = nums[slow_pointer]
        fast_pointer = nums[fast_pointer]
    return fast_pointer

a = [1,3,4,2,2]
print(find_duplicate(a))

