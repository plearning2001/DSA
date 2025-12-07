nums2 = [1,3]
nums3 = [3,1,2,4]
nums1 = [1,0,3]
nums6 = [0,2]
nums5 = [0,1]
nums4 = [0]
nums7 = [0,2,1]
nums8 = [0,1,2]
nums9 = [0,2,1,4]
nums = nums6

i = 0
j = len(nums)-1

while i<j:
    if nums[i]%2 == 0:
        i += 1
    elif nums[j]%2 == 1:
        j -=1 
    else: #nums[j]%2 == 0:
        nums[j],nums[i] = nums[i],nums[j]
        i += 1
        j -= 1
    

print(nums)

'''
[3,1,2,4]
 
'''