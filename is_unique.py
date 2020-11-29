#  method 1: brute force
#  time complexity: o(n^2)
#  space complexity: o(1)
def is_unique1(s):
    s = s.lower()
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return False
    return True

#  method 2: hash table
#  time complexity: o(n)
#  space complexity: o(n)
def is_unique2(s):
    s = s.lower()
    ht = dict()
    for i in s:
        if i not in ht:
            ht[i] = 1
        else:
            return False
    return True
#  time complexity: o(n)
#  space complexity: o(1)
#  method 3: use set function in python
def is_unique3(s):
    return len(set(s)) == len(s)

#  time complexity: o(n)
#  space complexity: o(1)
#  method 4: define alphabet
def is_unique4(s):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in s:
        if i in alpha:
            alpha.replace(i, '')
        else:
            return False
    return True


s1 ='abcd'
print(is_unique1(s1))
print(is_unique2(s1))
print(is_unique3(s1))
print(is_unique4(s1))