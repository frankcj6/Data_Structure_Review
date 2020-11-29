def largest_rec(heights):
    stack = [0]
    heights.append(0)

    res =0
    for right in range(1, len(heights)):
        while stack and heights[stack[-1]]>heights[right]:
            h = heights[stack.pop()]
            left = -1 if not stack else stack[-1]
            w = right - left -1
            res = max(res, h*w)
        stack.append(right)
    return res

A = [2,1,5,6,2,3]
print(largest_rec(A))