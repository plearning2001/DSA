# contains-duplicate-ii

nums = [1,2,3,1]
k = 3
nums = [1,0,1,1]
k = 1

nums = [1,2,3,1,2,3]
k = 1

dict = {}
target = False
for i in range(len(nums)):
    if nums[i] in dict.keys():
        if i - dict[nums[i]] <= k:
            target = True
        else:
            dict[nums[i]] = i    
    else:
        dict[nums[i]] = i

print(target)