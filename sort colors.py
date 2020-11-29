#  Time Complexity: O(n)
def sort_colors(s1):
    i = 0
    l = 0
    r = len(s1)-1
    while i <= r:
        if s1[i]==0:
            if i== l:
                i += 1
                continue
            s1[l], s1[i], l= s1[i], s1[l], l+1
        elif s1[i] == 2:
            s1[r], s1[i], r = s1[i], s1[r], r-1
        else:
            i += 1
    return s1
s = [2, 0, 2, 1, 1, 0]
print(sort_colors(s))

#  Time Complexity: O(n^2)
def sort_color2(a):
    for j in range(len(a)-1, 0, -1):
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
    return a

b = [0,2,3,4,5,6,1,0,0,1]
print(sort_color2(b))


#  Time complexity: O(log n)
def sort_color3(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
# Find the middle point and devide it
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = sort_color3(left_list)
    right_list = sort_color3(right_list)
    return list(merge(left_list, right_list))

# Merge the sorted halves

def merge(left_half,right_half):

    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res

b = [0,2,3,4,5,6,1,0,0,1]
print(sort_color3(b))



