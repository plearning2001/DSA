# maximum-sum-of-distinct-subarrays-with-length-k

from collections import Counter


nums = [1,5,4,2,9,9,9]
k = 3

max_total = 0
# sum = 0

count_map = Counter(nums[:k])
curr_sum = sum(nums[:k])
print(count_map)

max_total = curr_sum if len(count_map) == k else 0

for j in range(k,len(nums)):
    curr_sum = curr_sum + nums[j]
    curr_sum = curr_sum - nums[j-k]

    count_map[nums[j-k]] -= 1
    count_map[nums[j]] += 1

    if count_map[nums[j-k]] == 0:
        del count_map[nums[j-k]]

    if len(count_map) == k:
        max_total = max(max_total,curr_sum)

print(max_total)