#  time complexity o(n)
#  memory complexity o(n)
def is_anagram(s1, s2):
    ht = dict()
    if len(s1) != len(s2):
        return False
    for i in s1:
        if i not in ht:
            ht[i] = 1
        else:
            ht[i] += 1
    for i in s2:
        if i in ht:
            ht[i] -= 1
        else:
            ht[i] = 1
    for i in ht:
        if ht[i] != 0:
            return False
    return True

#  time complexity o(log n)
#  memory complexity o(log n)
#  method 2:
def is_anagram2(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    if sorted(s1) == sorted(s2):
        return True
    return False

s1 = 'fairy tales'
s2 = 'rail safety'
print(is_anagram(s1, s2))
print(is_anagram2(s1, s2))