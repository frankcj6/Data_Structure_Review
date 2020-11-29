def count_cons(s):
    s = s.replace(' ','').lower()
    count = 0
    for i in s:
        if i not in 'aeiou':
            count += 1
    return count

def recursive_count(s):
    if s == '':
        return 0
    if s[0].lower() not in 'aeiou' and s[0].isalpha():
        return 1 + recursive_count(s[1:])
    else:
        return recursive_count(s[1:])
s = 'abc dF'
print(count_cons(s))
print(recursive_count(s))
