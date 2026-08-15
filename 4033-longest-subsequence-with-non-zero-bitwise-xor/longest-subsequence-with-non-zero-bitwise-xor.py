class Solution(object):
    def longestSubsequence(self, nums):
        n = len(nums)
        total_xor = 0
        has_non_zero = False

        for x in nums:
            total_xor ^= x

            if x != 0:
                has_non_zero = True

        # Entire array already has non-zero XOR
        if total_xor != 0:
            return n

        # XOR is zero, but we have a non-zero element.
        # Remove that one element.
        if has_non_zero:
            return n - 1

        # All elements are zero
        return 0