class Solution(object):
    def mergeAlternately(self, word1, word2):
        ans = []

        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                ans.append(word1[i])

            if i < len(word2):
                ans.append(word2[i])

        return ''.join(ans)