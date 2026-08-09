class Solution(object):
    def largestSubmatrix(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        height = [0] * n
        ans = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    height[j] += 1
                else:
                    height[j] = 0

            arr = sorted(height, reverse=True)

            for j in range(n):
                ans = max(ans, arr[j] * (j + 1))

        return ans