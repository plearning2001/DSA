# maximum-average-subarray

import sys

nums = [1,12,-5,-6,50,3]
k = 4

nums = [5]
k = 1

i = 0
j = 0
max_avg = -(sys.maxsize)

curr_sum = 0
for i in range(0,k):
    curr_sum = curr_sum + nums[i]
max_avg = max(max_avg,curr_sum/k)

for j in range(k,len(nums)):
    curr_sum = curr_sum + nums[j]
    curr_sum = curr_sum - nums[j-k]
    max_avg = max_avg = max(max_avg,curr_sum/k)

print(round(max_avg,5))