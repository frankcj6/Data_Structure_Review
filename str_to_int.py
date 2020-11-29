def str_to_int(s):
    output_int = 0
    if s[0] == '-':
        i = 1
        is_negative = True
    else:
        i = 0
        is_negative = False
    for i in range(i, len(s)):
        e = 10**(len(s)-(i+1))
        digit = ord(s[i])-ord('0')
        output_int += e*digit
    if is_negative:
        return output_int * -1
    else:
        return output_int

s1 = '12345'
s2 ='0'
print(str_to_int(s1))
print(str_to_int(s2))
