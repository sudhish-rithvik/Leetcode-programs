class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = [0, 0, 0]
        left = 0
        ans = 0

        for right, ch in enumerate(s):
            count[ord(ch) - ord('a')] += 1

            while all(count):
                ans += len(s) - right
                count[ord(s[left]) - ord('a')] -= 1
                left += 1

        return ans