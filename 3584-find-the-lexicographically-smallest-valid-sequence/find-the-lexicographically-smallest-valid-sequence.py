class Solution(object):
    def validSequence(self, word1, word2):
        n = len(word1)
        m = len(word2)

        exact = [0] * (n + 1)
        almost = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            exact[i] = exact[i + 1]
            almost[i] = almost[i + 1]

            if exact[i + 1] < m:
                if word1[i] == word2[m - exact[i + 1] - 1]:
                    exact[i] = exact[i + 1] + 1

            if almost[i + 1] < m:
                if word1[i] == word2[m - almost[i + 1] - 1]:
                    almost[i] = almost[i + 1] + 1

            if exact[i + 1] < m:
                almost[i] = max(almost[i], exact[i + 1] + 1)

        ans = []
        j = 0
        used = False

        for i in range(n):
            if j == m:
                break

            remaining = m - j - 1

            if used:
                if word1[i] == word2[j] and exact[i + 1] >= remaining:
                    ans.append(i)
                    j += 1
            else:
                if word1[i] == word2[j] and almost[i + 1] >= remaining:
                    ans.append(i)
                    j += 1
                elif word1[i] != word2[j] and exact[i + 1] >= remaining:
                    ans.append(i)
                    j += 1
                    used = True

        return ans if j == m else []