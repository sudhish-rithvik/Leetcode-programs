class Solution(object):
    def findMissingElements(self, nums):
        seen = set(nums)
        ans = []

        low = min(nums)
        high = max(nums)

        for num in range(low, high + 1):
            if num not in seen:
                ans.append(num)

        return ans