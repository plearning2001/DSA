intervals = [[0,2],[1,3],[2,4],[3,5],[4,6]]
intervals = [[1,100],[11,22],[1,11],[2,12]]
intervals = [[0,1],[3,4],[1,2]]
final_list = []
sorted_list = sorted(intervals, key=lambda x: x[1])
final_list.append(sorted_list[0])
removed_intervals = 0
prev_counter = 0
prev_end=sorted_list[0][1]

for l in range(1,len(sorted_list)):

    cur = sorted_list[l]
    
    if prev_end>cur[0]:
        removed_intervals += 1    

    else:

        prev_end = sorted_list[l][1]

print(removed_intervals)