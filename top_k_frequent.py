def top_k(nums, k):
    dic ={}
    for i in nums:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    dic = sorted(dic, key = dic.get)[::-1]
    res = dic[:k]
    return res

nums = [4,1,-1,2,-1,2,3]
print(top_k(nums, 2))