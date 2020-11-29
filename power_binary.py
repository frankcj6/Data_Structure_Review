def power(x, n):
    res, pos = 1, True
    if x==0:
        return 0
    elif n==0:
        return 1
    elif n<0:
        n*= -1
        pos = None
    while n!=0:
        if n%2 ==1:
            res *= x
        n//=2
        x*=x
    if pos:
        return res
    else:
        return 1/res
