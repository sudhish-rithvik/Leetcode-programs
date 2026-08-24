class Solution(object):
    def stoneGameVIII(self, stones):
        n = len(stones)

        # Build prefix sums
        for i in range(1, n):
            stones[i] += stones[i - 1]

        # Base case: taking all stones
        ans = stones[-1]

        # Work backwards
        for i in range(n - 2, 0, -1):
            ans = max(ans, stones[i] - ans)

        return ans
        