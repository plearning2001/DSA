'''
Your little sister wrote down her TV show timings for today (messy order):
[1,3], [8,10], [2,6], [15,18], [9,11]
You want to make a clean schedule — merge all overlapping shows into one block.

Expected Output:
[1,6], [8,11], [15,18]

'''
given_list = [[1,3], [8,10], [2,6], [15,18], [9,11]]
final_list = []

sorted_list = sorted(given_list, key = lambda x: x[0])
print(sorted_list)
final_list = [sorted_list[0]]

for data in sorted_list:
    prev =  final_list[-1]
    curr = data

    if prev[1] >= curr[0]:
        prev[1] = max(curr[1],prev[1])
    else:
        final_list.append(data)
print(final_list)        