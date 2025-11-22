nums1 = [2,0] 
m = 1
nums2 = [1]
n = 1
k = len(nums1)-1
final_length = m+n
i = m-1
j = n-1

while j >= 0:
    if i < 0:
        nums1[k] = nums2[j]
        j-=1
        k -= 1
    else:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i-=1
            
        else:
            nums1[k] = nums2[j]
            j-=1
        k-=1
print(nums1)
