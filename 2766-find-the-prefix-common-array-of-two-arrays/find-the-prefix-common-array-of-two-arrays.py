class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        seenA = set()
        seenB = set()
        ans = []

        common = 0

        for i in range(len(A)):
            seenA.add(A[i])
            seenB.add(B[i])

            if A[i] in seenB:
                common += 1

            if B[i] in seenA and B[i] != A[i]:
                common += 1

            ans.append(common)

        return ans