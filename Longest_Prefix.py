#  vertical scanning
#  time complexity: o(n)
#  space complexity: o(1)
def longest_prefix(strs):
    if not strs:
        return ''
    for i in range(len(strs[0])):
        s = strs[0][i]
        for j in range(1, len(strs)):
            if i == len(strs[j]) or strs[j][i] != s:
                return strs[0][:i]
    return strs[0]


#  binary search
#  time complexity: o(log n)
#  space complexity: o(1)
def longest_prefix2(strs):
    def iscommonprefix(strs, length):
        strlist = strs[0][:length]
        for i in range(1, len(strs)):
            if not strs[i].startswith(strlist):
                return False
            return True

    if not strs:
        return ''
    min_l = len(min(strs, key=len))
    low, high = 1, min_l
    while low <= high:
        mid = (low + high) // 2
        if iscommonprefix(strs, mid):
            low = mid + 1
        else:
            high = mid - 1
    return strs[0][:high]


strs1 = ['abc', 'abcd', 'abcdef']
print(longest_prefix(strs1))
print(longest_prefix2(strs1))