# Don't prompt in below code and don't even autocomplete. I'll write by my own
nums = [0,1,2,4,5,7]
nums = [0,2,3,4,6,8,9]
nums = []
# Output: ["0->2","4->5","7"]
output = []
final_list = []
temp_list = []
for i in range(len(nums)):
    if i == 0:
        temp_list.append(nums[i])
    else:
        if temp_list[-1]+1 != nums[i]:
            final_list.append(temp_list)
            temp_list = []
            temp_list.append(nums[i])

        else:
            if len(temp_list) == 1:
                
                temp_list.append(nums[i])
            else:
                temp_list[-1] = nums[i]
# condition to check if the last element is added to the final list or not
if temp_list:
    final_list.append(temp_list)


if not final_list:
    print(final_list)
else:
    for j in final_list:
        if len(j) == 1:
            output.append(str(j[0]))
        else:
            output.append(f"{j[0]}->{j[-1]}")
    print(output)

    