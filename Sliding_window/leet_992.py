# subarrays-with-k-different-integers

from collections import Counter

nums = [1,2,1,2,3]
k = 2

def count_at_most(k,nums):
    left = 0
    counter = Counter()

    at_most_k = 0

    for right in range(len(nums)):
        num = nums[right]
        counter[num] += 1

        while len(counter)>k:
            counter[nums[left]] -= 1
            
            if counter[nums[left]] == 0:
                del counter[nums[left]]
            left += 1
        
        at_most_k = at_most_k + (right - left + 1)
    
    return at_most_k

print(count_at_most(k,nums) - count_at_most(k-1,nums))