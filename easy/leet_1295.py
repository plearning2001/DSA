from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        total = 0
        for i in nums:
            if (len(str(i))) % 2 == 0:
                total +=1
        return total

a = Solution()
nums1 = [1,1,0,1,1,1]
nums2 = [12,345,2,6,7896]
nums = [555,901,482,1771]
answer = a.findNumbers(nums)
print(f"answer - {answer}")
