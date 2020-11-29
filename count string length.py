def count_string_length(s1):
    count = 0
    for i in s1:
        count += 1
    return count

def count_string_recursive(s1):
    if s1 == '':
        return 0
    return 1+ count_string_recursive(s1[1:])

s1 = 'abcdefg '
print(count_string_length(s1))
print(count_string_recursive(s1))
len(s1)