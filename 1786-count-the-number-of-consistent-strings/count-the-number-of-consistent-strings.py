class Solution(object):
    def countConsistentStrings(self, allowed, words):
        allowed_set = set(allowed)
        ans = 0

        for word in words:
            valid = True

            for ch in word:
                if ch not in allowed_set:
                    valid = False
                    break

            if valid:
                ans += 1

        return ans