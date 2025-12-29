nums = [2,7,11,15]
target = 9

dict = {}

for i in range(len(nums)):
    print(i)
    if target - nums[i] in dict.keys():
        print([i,dict[target - nums[i]]])
        break
    else:
        dict[nums[i]] = i