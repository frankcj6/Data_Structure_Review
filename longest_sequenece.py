def longest_sequence(nums):
    num_dic = set()
    for num in nums:
        num_dic.add(num)
    max_num = 0
    while num_dic:
        cur = num_dic.pop()
        count = 1
        low, high = cur-1, cur+1
        while low in num_dic:
            count += 1
            num_dic.remove(low)
            low -= 1
        while high in num_dic:
            count += 1
            num_dic.remove(high)
            high += 1
        max_num = max(count, max_num)
    return max_num
nums = [100, 4, 200, 1, 3, 2]
print(longest_sequence(nums))