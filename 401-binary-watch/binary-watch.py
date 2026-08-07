class Solution(object):
    def readBinaryWatch(self, turnedOn):
        ans = []

        for h in range(12):
            for m in range(60):
                if bin(h).count("1") + bin(m).count("1") == turnedOn:
                    ans.append("%d:%02d" % (h, m))

        return ans