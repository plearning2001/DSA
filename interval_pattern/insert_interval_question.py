'''
Your **weekly calendar** already has clean (sorted, non-overlapping) meetings:
```
[1,3], [6,9]
```
Boss adds a **new meeting** `[2,7]`.
Fit it in and merge whatever overlaps!

**Expected Output:** `[1,9]`
'''

def insert_interval(intervals, new):
    result = []
    i = 0
    n = len(intervals)

    # Zone 1: Add all intervals that END before new starts
    # (no overlap, completely to the LEFT)
    while i < n and intervals[i][1] < new[0]:
        result.append(intervals[i])
        i += 1

    # Zone 2: Merge all overlapping intervals with new
    while i < n and intervals[i][0] <= new[1]:
        new[0] = min(new[0], intervals[i][0])  # expand start
        new[1] = max(new[1], intervals[i][1])  # expand end
        i += 1
    result.append(new)   # add the big merged interval

    # Zone 3: Add all remaining intervals (to the RIGHT)
    while i < n:
        result.append(intervals[i])
        i += 1

    return result


# ✅ Test 1
print(insert_interval([[1,3],[6,9]], [2,7]))
# Output: [[1,9]] ✅

# ✅ Test 2
print(insert_interval([[1,2],[3,5],[6,7],[8,10]], [4,8]))
# Output: [[1,2],[3,10]] ✅

# ✅ Test 3: No overlap at all
print(insert_interval([[1,3],[6,9]], [11,15]))
# Output: [[1,3],[6,9],[11,15]] ✅
