class Solution(object):
    def stoneGameII(self, piles):
        n = len(piles)

        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        dp = {}

        def dfs(i, M):
            if i >= n:
                return 0

            if 2 * M >= n - i:
                return suffix[i]

            if (i, M) in dp:
                return dp[(i, M)]

            best = 0

            for x in range(1, 2 * M + 1):
                if i + x > n:
                    break

                # Current player gets everything remaining
                # except what the opponent can guarantee.
                opponent = dfs(i + x, max(M, x))
                best = max(best, suffix[i] - opponent)

            dp[(i, M)] = best
            return best

        return dfs(0, 1)