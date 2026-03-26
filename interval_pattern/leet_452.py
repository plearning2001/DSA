points = [[10,16],[2,8],[1,6],[7,12]]
points = [[1,2],[3,4],[5,6],[7,8]]
points = [[1,2],[2,3],[3,4],[4,5]]

sorted_points = sorted(points, key=lambda x: x[0])
print(f"sorted_points: {sorted_points}")
final_list = []

final_list.append(sorted_points[0])

for l in range(1,len(sorted_points)):
    if sorted_points[l][0] > final_list[-1][1]:
        final_list.append(sorted_points[l])
    else:
        final_list[-1][0] = max(final_list[-1][0], sorted_points[l][0])
        final_list[-1][1] = min(final_list[-1][1], sorted_points[l][1])
print(len(final_list))