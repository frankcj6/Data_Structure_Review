#  two pointer hash
def intersect_sort_array(s1, s2):
    i = 0
    j = 0
    intersection = []
    while i < len(s1) and j< len(s2):
        if s1[i] == s2[j]:
            intersection.append(s1[i])
            i += 1
            j += 1
        elif s1[i] < s2[j]:
            i += 1
        else:
            j += 1
    return intersection

s1 = [2, 2, 4, 5]
s2 = [2, 2, 3, 4]
print(intersect_sort_array(s1, s2))

#  Binary search
def intersection_binary(s, t):
    s.sort()
    t.sort()
    list = []
    if len(s)>=len(t):
        s,t = t, s

    for i in range(len(s)):
        target = s[i]
        l, r = 0, len(t)-1
        while l<= r:
            mid = (l+r)//2
            if t[mid] == target:
                list.append(target)
                t.pop(mid)
                r -= 1
                break
            elif t[mid] < target:
                l = mid + 1
            else:
                r = mid -1
    return list


s1 = [1, 2, 2, 1]
s2 = [2, 2]
print(intersection_binary(s1, s2))

def intersect_hash(nums1, nums2):
    dic ={}
    res = []
    for i in nums1:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    for i in nums2:
        if i in dic and dic[i]!= 0:
            res.append(i)
            dic[i] -= 1
    return res

s1 = [1, 2, 2, 1]
s2 = [2, 2]
print(intersect_hash(s1, s2))