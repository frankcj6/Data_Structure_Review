def Strstr(haystack, needle):
    i = 0
    j = 0
    if len(needle) == 0:
        return 0
    while i< len(haystack) and  len(haystack)-i+1 > len(needle):
        if haystack[i] == needle[j]:
            pos = i
            while j < len(needle) and needle[j] == haystack[i]:
                i += 1
                j += 1
            if j == len(needle):
                return pos
            i = pos+1
            j = 0
        else:
            i += 1
    return -1


def strstr2(haystack, needle):
    if not needle:
        return 0
    if len(haystack)< len(needle):
        return -1
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1


s1 = 'helloworld'
s2 = 'lo'
print(Strstr(s1, s2))
print(strstr2(s1, s2))