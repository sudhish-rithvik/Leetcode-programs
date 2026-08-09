class Solution(object):
    def getBiggestThree(self, grid):
        m = len(grid)
        n = len(grid[0])

        sums = set()

        for r in range(m):
            for c in range(n):
                # Rhombus of size 0 (single cell)
                sums.add(grid[r][c])

                k = 1

                while r + 2 * k < m and c - k >= 0 and c + k < n:
                    total = 0

                    # Top -> Right
                    for i in range(k):
                        total += grid[r + i][c + i]

                    # Right -> Bottom
                    for i in range(k):
                        total += grid[r + k + i][c + k - i]

                    # Bottom -> Left
                    for i in range(k):
                        total += grid[r + 2 * k - i][c - i]

                    # Left -> Top
                    for i in range(k):
                        total += grid[r + k - i][c - k + i]

                    sums.add(total)
                    k += 1

        return sorted(sums, reverse=True)[:3]