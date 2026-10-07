class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maximum = max(candies)
        ans = []

        for candy in candies:
            ans.append(candy + extraCandies >= maximum)

        return ans