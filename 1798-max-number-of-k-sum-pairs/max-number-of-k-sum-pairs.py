class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()

        left = 0
        right = len(nums) - 1
        ans = 0

        while left < right:
            total = nums[left] + nums[right]

            if total == k:
                ans += 1
                left += 1
                right -= 1
            elif total < k:
                left += 1
            else:
                right -= 1

        return ans