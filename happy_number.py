def happy_number(n):
    dic = {}
    sum = 0
    temp = n
    while (temp!= 1):
        while(n!= 0):
            x = n%10
            n = n//10
            sum += x*x
        temp = sum
        if temp in dic:
            return False
        else:
            dic[temp] = 1
        n = temp
        sum = 0
    return True

n = 19
print(happy_number(19))