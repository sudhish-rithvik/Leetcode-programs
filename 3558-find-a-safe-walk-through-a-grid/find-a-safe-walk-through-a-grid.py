from collections import deque
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = grid[0][0]

        q = deque([(0, 0)])

        while q:
            r, c = q.popleft()

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    new_health = dist[r][c] + grid[nr][nc]

                    if new_health < dist[nr][nc]:
                        dist[nr][nc] = new_health
                        q.append((nr, nc))

        return dist[m - 1][n - 1] < health