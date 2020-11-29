def is_palin_perm(s):
    s = s.replace(' ', '').lower()
    ht = dict()
    for i in s:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1
    odd_count = 0
    for k, v in ht.items():
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif v % 2 != 0 and odd_count != 0:
            return False
    return True

s1 = 'taco cat'
s2 = 'i am a'

print(is_palin_perm(s1))
print(is_palin_perm(s2))