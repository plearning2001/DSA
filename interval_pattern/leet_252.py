# meeting-schedule problem

intervals = [(0,30),(5,10),(15,20)]
if not intervals:
    print(True)
final_list = []
sorted_list = sorted(intervals, key=lambda x: x.start)

final_list.append(sorted_list[0])
status = True

for l in range(1,len(sorted_list)):

    cur = sorted_list[l]

    prev = final_list[len(final_list)-1]


    if prev.end<=cur.start:
        final_list.append(cur)
        
    else:
        status = False
        break
    
print(status)