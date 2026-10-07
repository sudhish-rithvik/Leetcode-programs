class Solution(object):
    def mapWordWeights(self, words, weights):
        ans = []

        for word in words:
            total = 0

            for ch in word:
                total += weights[ord(ch) - ord('a')]

            remainder = total % 26

            # Reverse alphabet mapping
            ans.append(chr(ord('z') - remainder))

        return ''.join(ans)