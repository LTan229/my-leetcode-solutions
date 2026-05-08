---
Tags:
  - SQL
Languages:
  - SQL
URL:
---
# Visited
```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        visited = [[0] * n for _ in range(m)]
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def valid(i, j):
            return 0 <= i < m and 0 <= j < n 
        
        results = []
        i, j = 0, 0
        d = 0
        while True:
            results.append(matrix[i][j])
            visited[i][j] = 1
            # go next
            nexti, nextj = i + dirs[d][0], j + dirs[d][1]
            # if valid and not visited, go next
            if valid(nexti, nextj) and (not visited[nexti][nextj]):
                i, j = nexti, nextj
                continue
            # turn and go next
            print(d, (d + 1) % 4)
            d = (d + 1) % 4
            nexti, nextj = i + dirs[d][0], j + dirs[d][1]         # if valid and not visited, go next
            if valid(nexti, nextj) and (not visited[nexti][nextj]):
                i, j = nexti, nextj
                continue
            
            break

        return results
```

# Boundary

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        results = []

        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while True:
            for i in range(left, right + 1):
                results.append(matrix[top][i])
            top += 1 
            if top > bottom: break

            for i in range(top, bottom + 1):
                results.append(matrix[i][right])
            right -= 1
            if left > right: break

            for i in range(right, left - 1, -1):
                results.append(matrix[bottom][i])
            bottom -= 1
            if top > bottom: break
            
            for i in range(bottom, top - 1, -1):
                results.append(matrix[i][left])
            left += 1
            if left > right: break
            
        return results
```