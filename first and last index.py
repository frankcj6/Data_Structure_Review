# need to find first and last
firstindex = -1
start1 = 0
end1 = len(nums) - 1
while (start1 <= end1):
    middle = (start1 + end1) // 2
    if nums[middle] >= target:
        if nums[middle] == target:
            firstindex = middle
        end1 = middle - 1
    else:
        start1 = middle + 1

secondindex = -1
start2 = 0
end2 = len(nums) - 1
while (start2 <= end2):
    middle = (start2 + end2) // 2
    if nums[middle] <= target:
        if nums[middle] == target:
            secondindex = middle
        start2 = middle + 1
    else:
        end2 = middle - 1

return [firstindex, secondindex]