class Solution(object):
    def countMaxOrSubsets(self, nums):
        target = 0

        for num in nums:
            target |= num

        count = [0]

        def dfs(i, current):
            if i == len(nums):
                if current == target:
                    count[0] += 1
                return

            # Don't take nums[i]
            dfs(i + 1, current)

            # Take nums[i]
            dfs(i + 1, current | nums[i])

        dfs(0, 0)

        return count[0]
        