def merge_interval(intervals):
    intervals.sort()
    i = 0
    n = len(intervals)
    results = []
    while i <n:
        low = intervals[i][0]
        high = intervals[i][1]
        while i<n-1 and intervals[i+1][0]<=high:
            high = max(high, intervals[i+1][1])
            i += 1
        results.append([low, high])
        i+= 1
    return results


def merge_sort_2(intervals):
    intervals.sort()
    i = 0
    n = len(intervals)
    insert_idx = 0
    while i < n:
        low = intervals[i][0]
        high = intervals[i][1]
        while i< n-1 and intervals[i+1][0]<=high:
            high = max(high, intervals[i+1][1])
            i += 1
        intervals[insert_idx] = [low, high]
        insert_idx += 1
        i += 1
    while (len(intervals)>insert_idx):
        intervals.pop()
    return intervals


intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge_sort_2(intervals))
