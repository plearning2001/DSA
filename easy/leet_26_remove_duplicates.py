nums = [1,1,2]
expectedNums = []
i = 0
j = 1
length = 0

while j != len(nums):
    if nums[i] == nums[j]:
        j += 1
    else:
        nums[i+1],nums[j] = nums[j],nums[i+1]
        i += 1
        j += 1

print(i+1)
