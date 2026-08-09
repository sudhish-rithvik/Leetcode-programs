class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()

        i = 0

        for cookie in s:
            if i < len(g) and cookie >= g[i]:
                i += 1

        return i