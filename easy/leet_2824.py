nums1 = [-1,1,2,3,1]
target1 = -2
nums = [-6,2,5,-2,-7,-1,3]
target = -2


nums.sort()
print(nums)


i = 0
j = len(nums)-1

count = 0

while i<j:
    if nums[j]+nums[i]<target:
        count = count + (j-i)
        i += 1
    elif nums[j]+nums[i]>=target:
        j -= 1

print(f"No. of pairs -- {count}")