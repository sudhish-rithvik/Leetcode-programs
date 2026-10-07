class Solution(object):
    def validStrings(self, n):
        ans = []

        def backtrack(s):
            if len(s) == n:
                ans.append(s)
                return

            # Add 1
            backtrack(s + "1")

            # Add 0 only if previous character is not 0
            if not s or s[-1] != "0":
                backtrack(s + "0")

        backtrack("")

        return ans
        