from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        right_sum = 0
        for i in nums:
            right_sum = right_sum+i
        print(right_sum)

        left_sum = 0
        for j in nums:
            if left_sum == right_sum-j:
                return nums.index(j)
            else:
                left_sum = left_sum + j
                right_sum = right_sum-j
        return -1


answer_object = Solution()
nums1 = [1,2,3]
nums2 = [12,345,2,6,7896]
nums = [2,1,-1]
answer = answer_object.pivotIndex(nums)
print(f"answer - {answer}")
