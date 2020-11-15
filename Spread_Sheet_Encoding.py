def spread_sheet_encoding(col_str):
    num = 0
    count = len(col_str)-1
    for s in col_str:
        num += 26**count*(ord(s)-ord('A')+1)
        count -= 1
    return num


print(spread_sheet_encoding('A'))
print(spread_sheet_encoding('ABCD'))
