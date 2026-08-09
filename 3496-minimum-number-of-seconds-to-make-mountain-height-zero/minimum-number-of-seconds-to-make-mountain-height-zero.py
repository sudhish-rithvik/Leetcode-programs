class Solution(object):
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        def can_finish(seconds):
            total = 0

            for t in workerTimes:
                # Maximum x such that:
                # t * x * (x + 1) / 2 <= seconds
                x = int(((2.0 * seconds / t + 0.25) ** 0.5) - 0.5)

                total += x

                if total >= mountainHeight:
                    return True

            return False

        left = 0
        right = min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2

        while left < right:
            mid = (left + right) // 2

            if can_finish(mid):
                right = mid
            else:
                left = mid + 1

        return left