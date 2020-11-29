def count_longest_substring(a):
    ht = dict()
    res = 0
    l = 0
    for r in range(len(a)):
        if a[r] not in ht:
            ht[a[r]] = 1
            res = max(res, r-l+1)
        else:
            while a[l] != a[r]:
                ht.pop(a[l])
                l += 1
            l += 1
    return res