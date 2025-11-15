from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        local_counter = 0
        global_counter = 0
        for i in nums:
            if i == 1:
                local_counter += 1
                if global_counter < local_counter:
                    global_counter = local_counter
            else:
                local_counter = 0
        print(f"global_counter - {global_counter}")
        return global_counter
a = Solution()
nums1 = [1,1,0,1,1,1]
nums2 = [0,0,0,0]
nums = [1,1,1,1,1,1,1,1]
answer = a.findMaxConsecutiveOnes(nums)
print(f"answer - {answer}")
