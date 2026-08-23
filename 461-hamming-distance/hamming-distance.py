class Solution(object):
    def hammingDistance(self, x, y):
        x = x ^ y
        count = 0

        while x:
            x = x & (x - 1)
            count += 1

        return count