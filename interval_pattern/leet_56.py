intervals = [[1,3],[2,6],[8,10],[15,18]]
final_list = []
sorted_list = sorted(intervals, key=lambda x: x[0])
final_list.append(sorted_list[0])

for l in range(1,len(sorted_list)):

    cur = sorted_list[l]
    prev = final_list[len(final_list)-1]


    if prev[1]<cur[0]:
        final_list.append(cur)
        
    else:
        prev[0] = min(prev[0],cur[0])
        prev[1] = max(prev[1],cur[1])
    
print(final_list)