class Solution(object):
    def countSubmatrices(self, grid, k):
        m = len(grid)
        n = len(grid[0])

        ans = 0
        prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = (
                    grid[i - 1][j - 1]
                    + prefix[i - 1][j]
                    + prefix[i][j - 1]
                    - prefix[i - 1][j - 1]
                )

                if prefix[i][j] <= k:
                    ans += 1

        return ans