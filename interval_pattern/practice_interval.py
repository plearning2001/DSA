
def intersect(a, b):
    start = max(a[0], b[0])   # latest start
    end   = min(a[1], b[1])   # earliest end
    # valid only if start <= end (otherwise no overlap)
    if start <= end:
        return [start, end]
    return None   # no intersection


print(intersect([2, 8], [5, 10])) 
print(intersect([1, 4], [6, 9]))  
print(intersect([1, 7], [3, 5]))  