# minimum-size-subarray-sum

import sys
nums = [2,3,1,2,4,3]
target = 7

min_size = sys.maxsize
max_int = sys.maxsize

for i in range(0,len(nums)):
    curr_sum = 0
    for j in range(i,len(nums)):
        curr_sum = curr_sum + nums[j]
        if curr_sum >= target:
            min_size = min(min_size,j-i+1)

if min_size == max_int:
    min_size = 0

print(min_size)