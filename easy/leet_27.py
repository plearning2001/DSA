nums = [3,2,2,3]
val = 3

index = 0
for i in range(len(nums)):
    if nums[i] != val:
        nums[index] = nums[i]
        index += 1
print(index)