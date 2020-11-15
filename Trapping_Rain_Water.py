#  solution to leetcode 42
#  solution 1: DP
#  Time Complexity: O(n)
#  Space Complexity: O(n)


def trap(self, height):
    if not height:
        return -1
    ans = 0
    for i in range(1, len(height)-1):
        left_max = max(height[:i])
        right_max = max(height[i + 1:])
        area = min(left_max, right_max) - height[i]
        ans += max(0, area)
    return ans


#  Solution 2: Stacks
#  Time Complexity: O(N)
#  Space Complexity: O(N)

def trap_stack(self, height):
    if not height:
        return -1
    stack = []
    area = 0
    for i in range(len(height)):
        offset = 0
        while stack and height[i] > height[stack[-1]]:
            previous_index = stack.pop()
            area += (height[previous_index]-offset)*(i-previous_index-1)
            offset = height[previous_index]
        if stack:
            area += (height[i]-offset)*(i-stack[-1]-1)
        stack.append(i)
    return area


#  Solution 3: Two Pointers
#  Time Complexity: O(N)
#  Space Complexity: O(1)

def trap_stack(self, height):
    left, right = 0, len(height)-1
    left_wall, right_wall = 0, 0
    ans = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] > left_wall:
                left_wall = height[left]
            else:
                ans += left_wall - height[left]
            left += 1
        else:
            if height[right] > right_wall:
                right_wall = height[right]
            else:
                ans += right_wall - height[right]
            right -= 1
    return ans

