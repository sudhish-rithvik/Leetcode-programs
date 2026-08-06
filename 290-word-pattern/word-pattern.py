class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()

        if len(pattern) != len(words):
            return False

        p_map = {}
        w_map = {}

        for p, w in zip(pattern, words):
            if p in p_map and p_map[p] != w:
                return False
            if w in w_map and w_map[w] != p:
                return False

            p_map[p] = w
            w_map[w] = p

        return True