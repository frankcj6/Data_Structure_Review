def pascal_tri(numRows):
    if numRows<1:
        return []
    current = 1
    res = []
    row = []
    if current == 1:
        row.append(1)
        res.append(row)
        row = []
    while current < numRows:
        prevRow = res[current-1]
        for i in range(current+1):
            if i== 0 or i == current:
                row.append(1)
            else:
                row.append(prevRow[i]+prevRow[i-1])
        res.append(row)
        row = []
        current += 1
    return res


print(pascal_tri(4))

