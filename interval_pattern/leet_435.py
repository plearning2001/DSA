intervals = [[1,100],[11,22],[1,11],[2,12]]
final_list = []
sorted_list = sorted(intervals, key=lambda x: x[0])
final_list.append(sorted_list[0])
removed_intervals = 0

for l in range(1,len(sorted_list)):

    cur = sorted_list[l]
    prev = final_list[-1]
    if prev[1]>cur[0]:
        removed_intervals += 1    
        if prev[1]>cur[1]:
            prev[0] = cur[0]
            prev[1] = cur[1]

    else:

        final_list.append(cur)

print(len(intervals) - len(final_list))