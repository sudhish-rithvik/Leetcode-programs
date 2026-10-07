class Solution(object):
    def maxFreqSum(self, s):
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        vowels = set("aeiou")
        max_vowel = 0
        max_consonant = 0

        for ch in count:
            if ch in vowels:
                max_vowel = max(max_vowel, count[ch])
            else:
                max_consonant = max(max_consonant, count[ch])

        return max_vowel + max_consonant