class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        ans = 0

        for x in nums1:
            for y in nums2:
                if x % (y * k) == 0:
                    ans += 1

        return ans