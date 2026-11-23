from typing import List
from collections import deque

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        graph = [[] for _ in range(n)]
        indegree = [0] * n

        for u, v, w in edges:
            if online[u] and online[v]:
                graph[u].append((v, w))
                indegree[v] += 1

        q = deque(i for i in range(n) if indegree[i] == 0)
        topo = []

        while q:
            u = q.popleft()
            topo.append(u)

            for v, w in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        def check(limit):
            INF = float('inf')
            dp = [INF] * n
            dp[0] = 0

            for u in topo:
                if dp[u] == INF:
                    continue

                for v, w in graph[u]:
                    if w >= limit:
                        dp[v] = min(dp[v], dp[u] + w)

            return dp[n - 1] <= k

        left, right = 0, 10**9
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans