def add_one(digits):
    if len(digits) == 1 and digits[0] == 9:
        return [1, 0]
    digits[-1] += 1
    for i in range(len(digits)-1, 0, -1):
        if digits[i] == 10:
            digits[i] = 0
            digits[i - 1] += 1
            if digits[0] == 10:
                digits[0] = 0
                digits = [1] + digits
    return digits

A = [9, 9, 9]
print(add_one(A))


def add_one_2(digits):
    i = len(digits)-1
    while i>= 0:
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            break
        i -= 1
    if i == -1:
        digits = [1] + [0] * len(digits)
    return digits

print(add_one_2(A))
