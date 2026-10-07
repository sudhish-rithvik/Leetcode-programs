class Solution(object):
    def largestLocal(self, grid):
        n = len(grid)
        ans = []

        for i in range(n - 2):
            row = []

            for j in range(n - 2):
                maximum = 0

                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        maximum = max(maximum, grid[x][y])

                row.append(maximum)

            ans.append(row)

        return ans