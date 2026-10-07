class Solution(object):
    def leftRightDifference(self, nums):
        total = sum(nums)
        left = 0
        ans = []

        for num in nums:
            total -= num       # now total = right sum
            ans.append(abs(left - total))
            left += num

        return ans