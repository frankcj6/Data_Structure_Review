def find_first_upper_iterative(str):
    for i in str:
        if i.isupper():
            return i
    return 'No Upper Letter'


def find_first_upper_recursive(s, i=0):
    if s[i].isupper():
        return s[i]
    if i == len(s)-1:
        'No upper letter'
    return find_first_upper_recursive(s, i+1)


str = 'aBcCs'
print(find_first_upper_iterative(str))
print(find_first_upper_recursive(str))