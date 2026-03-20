def max_overlapping(intervals):
    events = []

    for start, end in intervals:
        events.append((start, +1))   # interval starts → +1
        events.append((end,   -1))   # interval ends   → -1
    print(f"before events -- {events}")
    # Sort by time
    # If same time → process -1 before +1 (end before start)
    events.sort(key=lambda x: (x[0], x[1]))
    print(f"after events -- {events}")
    max_count = 0
    count = 0

    for time, change in events:
        count += change
        max_count = max(max_count, count)

    return max_count


# ✅ Test it!
print(max_overlapping([[1,4],[2,6],[3,5]]))   # 3 ✅
print(max_overlapping([[1,2],[2,7],[6,8]]))   # 2 ✅
print(max_overlapping([[1,2],[3,4],[5,6]]))   # 1 ✅ (no overlaps)