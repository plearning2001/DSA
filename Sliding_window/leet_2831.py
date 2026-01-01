class Solution:
    def longestEqualSubarray(self, nums, k):
        freq = {}
        left = 0
        max_freq = 0
        answer = 0

        for right in range(len(nums)):
            num = nums[right]
            freq[num] = freq.get(num, 0) + 1
            max_freq = max(max_freq, freq[num])

            while (right - left + 1) - max_freq > k:
                freq[nums[left]] -= 1
                left += 1

            answer = max(answer, max_freq)

        return answer

s = Solution()

nums = [1,3,2,3,1,3]
k = 3

print(s.longestEqualSubarray(nums,k))
