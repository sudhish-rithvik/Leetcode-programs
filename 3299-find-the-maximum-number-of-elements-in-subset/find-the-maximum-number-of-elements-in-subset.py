class Solution(object):
    def maximumLength(self, nums):
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        ans = 1

        if 1 in count:
            ones = count[1]
            if ones % 2 == 0:
                ones -= 1
            ans = max(ans, ones)

        for num in count:
            if num == 1:
                continue

            x = num
            length = 0

            while count.get(x, 0) >= 2:
                length += 2
                x = x * x

            if count.get(x, 0) >= 1:
                length += 1
            else:
                length -= 1

            ans = max(ans, length)

        return ans