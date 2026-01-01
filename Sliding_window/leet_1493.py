# longest-subarray-of-1s-after-deleting-one-element

nums = [1,1,1]
k = 1

left = 0

ones = 0
max_len = 0

for right in range(len(nums)):
    num = nums[right] 
    if num == 1:
        ones += 1

    while (right-left+1) - ones > 1:
        if nums[left] == 1:
            ones -= 1
        left += 1

    max_len = max(max_len,right-left)

print(max_len)


