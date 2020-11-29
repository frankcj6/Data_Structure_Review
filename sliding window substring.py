import collections


def min_window(s, t):
    count = collections.Counter(t)
    slow = start = parts = 0
    minlen = float('inf')
    for fast in range(len(s)):
        if s[fast] in count:
            count[s[fast]] -= 1
            if count[s[fast]] >= 0:
                parts += 1

        while parts == len(t):
            if minlen > fast - slow + 1:
                minlen = fast - slow + 1
                start = slow
            if s[slow] in count:
                count[s[slow]] += 1
                if count[s[slow]] > 0:
                    parts -= 1
            slow += 1
    return s[start:(start + minlen)] if minlen != float('inf') else ''


s1 = 'ADOBECODEBANC'
t1 = 'ABC'
print(min_window(s1, t1))

#  solution 2:

