# minimum-size-subarray-sum brute force
'''
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
'''

# minimum-size-subarray-sum Sliding window

import sys
nums = [2,3,1,2,4,3]
target = 7

min_size = sys.maxsize
max_int = sys.maxsize

i = 0
j = 0
curr_sum = 0

while j < len(nums):
    curr_sum = curr_sum + nums[j]
    while (curr_sum >= target):
        min_size = min(min_size,j-i+1)
        curr_sum = curr_sum - nums[i]
        i += 1
    j += 1

if min_size == max_int:
    min_size = 0

print(min_size)