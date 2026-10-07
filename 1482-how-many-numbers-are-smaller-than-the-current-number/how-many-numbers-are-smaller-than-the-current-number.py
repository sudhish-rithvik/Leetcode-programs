class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        count = [0] * 101

        # Frequency of each number
        for num in nums:
            count[num] += 1

        # Prefix sum: count[i] = numbers <= i
        for i in range(1, 101):
            count[i] += count[i - 1]

        ans = []

        for num in nums:
            if num == 0:
                ans.append(0)
            else:
                ans.append(count[num - 1])

        return ans