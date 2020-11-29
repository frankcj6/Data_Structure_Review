
#  Method 1:
#  Time complexity: o(log n)
#  space complexity: o (1)
def check_perm1(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) != len(s2):
        return False
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))
    n = len(s1)
    for i in range(n):
        if s1[i] != s2[i]:
            return False
    return True

def check_perm2(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    ht = dict()
    if len(s1) != len(s2):
        return False
    for i in s1:
        if i not in ht:
            ht[i] = 1
        else:
            ht[i] += 1
    for i in s2:
        if i not in ht:
            ht[i] = 1
        else:
            ht[i] -= 1
    return all(value == 0 for value in ht.values())

string1 = 'google'
string2 = 'ooggle'
print(check_perm1(string1, string2))
print(check_perm2(string1, string2))