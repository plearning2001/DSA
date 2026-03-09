# Merged interval = [min of starts, max of ends]

def merge_two(a, b):
    start = min(a[0], b[0])   # earliest start
    end   = max(a[1], b[1])   # latest end
    return [start, end]

# print(merge_two([2, 6], [4, 9]))
# print(merge_two([1, 5], [3, 4]))
# print(merge_two([1, 4], [4, 8]))


# Intersection

def intersect(a, b):
    start = max(a[0], b[0])   # earliest start
    end   = min(a[1], b[1])   # latest end
    if start <= end:
        return [start, end]
    else:
        return None

print(intersect([2, 8], [5, 10]))
print(intersect([1, 4], [6, 9]))
print(intersect([1, 7], [3, 5]))


def intersect(a, b):
    start = max(a[0], b[0])   # latest start
    end   = min(a[1], b[1])   # earliest end
    # valid only if start <= end (otherwise no overlap)
    if start <= end:
        return [start, end]
    return None   # no intersection


# print(intersect([2, 8], [5, 10])) 
# print(intersect([1, 4], [6, 9]))  
# print(intersect([1, 7], [3, 5]))  