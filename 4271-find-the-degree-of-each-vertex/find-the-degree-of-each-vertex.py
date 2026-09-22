class Solution(object):
    def findDegrees(self, matrix):
        ans = []

        for row in matrix:
            ans.append(sum(row))

        return ans