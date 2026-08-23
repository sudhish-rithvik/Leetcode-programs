class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        if duration == 0:
            return 0

        ans = duration

        for i in range(1, len(timeSeries)):
            gap = timeSeries[i] - timeSeries[i - 1]
            ans += min(gap, duration)

        return ans