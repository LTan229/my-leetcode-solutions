---
Tags:
  - BFS
  - 数组
  - 矩阵
  - H100
Languages:
  - Python
URL: https://leetcode.cn/problems/rotting-oranges/?envType=study-plan-v2&envId=top-100-liked
---

```python
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        arr = deque([])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        time = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    arr.append((i, j, 0))
        
        while arr:
            i, j, t = arr.popleft()
            time = max(time, t)
            for d in dirs:
                newi = i + d[0]
                newj = j + d[1]
                if 0 <= newi < n and 0 <= newj < m and grid[newi][newj] == 1:
                    grid[newi][newj] = 2 # you only look once
                    arr.append((newi, newj, t + 1))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        
        return time
```