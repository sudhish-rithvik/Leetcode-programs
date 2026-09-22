class Solution(object):
    def minimumOperations(self, nums):
        ans = 0

        for num in nums:
            if num % 3 != 0:
                ans += 1

        return ans
        