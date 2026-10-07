class Solution(object):
    def findArray(self, pref):
        ans = [pref[0]]

        for i in range(1, len(pref)):
            ans.append(pref[i - 1] ^ pref[i])

        return ans