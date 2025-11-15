from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        right_sum = 0
        for i in nums:
            right_sum = right_sum+i
        print(right_sum)

        left_sum = 0
        for j in range(len(nums)):
            if left_sum == right_sum-nums[j]:
                return j
            else:
                left_sum = left_sum + nums[j]
                right_sum = right_sum - nums[j]
        return -1


answer_object = Solution()
nums1 = [1,2,3]
nums2 = [12,345,2,6,7896]
nums3 = [2,1,-1]
nums4 = [-1,-1,-1,-1,-1,0]
nums = [-1,-1,0,1,1,0]



answer = answer_object.pivotIndex(nums)
print(f"answer - {answer}")
