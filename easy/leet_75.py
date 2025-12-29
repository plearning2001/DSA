nums = [2,0,2,1,1,0,0,2,1,2,1,0]

i = k = 0
j = len(nums)-1

while k<=j:
    if nums[k] == 2:
        nums[k],nums[j] = nums[j],nums[k]
        j -= 1
    elif nums[k] == 0:
        nums[k],nums[i] = nums[i],nums[k]
        i += 1
        k += 1
    else:
        k += 1
print(nums)