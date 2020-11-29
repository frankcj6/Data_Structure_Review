def divide(divider, divisor):
    if divider ==0:
        return 0
    l = 0
    r = 2**32 -1
    pos = 1
    if divider<0:
        pos *= -1
        divider = abs(divider)
    if divisor<0:
        pos *= -1
        divisor = abs(divisor)
    while l<= r:
        mid = l+ (r-l)//2
        if mid*divisor<= divider<(mid+1)*divisor:
            if pos<0:
                return mid*pos
            else:
                return min(mid, 2**31-1)*pos
        if divider <= mid*divisor:
            r = mid -1
        elif divider>=(mid+1)*divisor:
            l = mid + 1


print(divide(7, -3))