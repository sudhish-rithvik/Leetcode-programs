class Solution(object):
    def numIdenticalPairs(self, nums):
        count = {}
        ans = 0

        for num in nums:
            if num in count:
                ans += count[num]

            count[num] = count.get(num, 0) + 1

        return ans
        