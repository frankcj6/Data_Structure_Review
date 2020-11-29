def merge_sort(nums1, m, nums2, n):
    idx = m + n - 1
    i, j = m - 1, n - 1
    while i >= 0 or j >= 0:
        if i < 0:
            nums1[idx] = nums2[j]
            j -= 1
        elif j < 0:
            nums1[idx] = nums1[i]
            i -= 1
        elif nums1[i] > nums2[j]:
            nums1[idx] = nums1[i]
            i -= 1
        else:
            nums1[idx] = nums2[j]
            j -= 1
        idx -= 1
    return nums1
