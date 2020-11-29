def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1

        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True

s = 'Abc cba'
print(is_palindrome(s))


def is_palindrome2(s):
    s = [i.lower() for i in s if i.isalnum()]
    i = 0
    stack = []
    while i < len(s) // 2:
        stack.append(s[i])
        i += 1
    if len(s) % 2 != 0:
        i += 1
    while i < len(s):
        ele = stack.pop()
        if ele != s[i]:
            return False
        i += 1
    return True



s1 = 'ann:a'
print(is_palindrome2(s1))
