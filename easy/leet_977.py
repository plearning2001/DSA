nums1 = [-5,-3,-2,-1]
nums = [-4,-1,0,3,10]

i = 0
j = len(nums)-1
final = [0]*len(nums)
k = len(final)-1

while i<=j:
    if abs(nums[i]) >abs(nums[j]):
        final[k] = nums[i]*nums[i]
        i += 1
        k -= 1
    elif abs(nums[i]) <= abs(nums[j]):
        final[k] = nums[j]*nums[j]
        j -= 1
        k -= 1
print(final)