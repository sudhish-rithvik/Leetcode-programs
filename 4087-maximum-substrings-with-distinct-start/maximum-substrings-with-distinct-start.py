class Solution(object):
    def maxDistinct(self, s):
        seen = set()

        for ch in s:
            seen.add(ch)

        return len(seen)