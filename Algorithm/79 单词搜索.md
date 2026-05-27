---
Tags:
  - DFS
  - 数组
  - 字符串
  - 回溯
  - 矩阵
  - H100
Languages:
  - Python
URL: https://leetcode.cn/problems/word-search/description/?envType=study-plan-v2&envId=top-100-liked
---
# 优化版
```python
from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])

        board_counts = Counter(char for row in board for char in row)
        word_counts = Counter(word)
        for char, count in word_counts.items():
            if board_counts[char] < count:
                return False # 频率剪枝
        
        if board_counts[word[0]] > board_counts[word[-1]]:
            word = word[::-1] # 首字母剪枝

        def searchfrom(i, j, idx):
            if idx == len(word):
                return True

            if not (0 <= i < n 
                and 0 <= j < m 
                and board[i][j] == word[idx]):
                return False

            temp = board[i][j]
            board[i][j] = '.'

            result = (searchfrom(i + 1, j, idx + 1) or 
                    searchfrom(i - 1, j, idx + 1) or 
                    searchfrom(i, j + 1, idx + 1) or 
                    searchfrom(i, j - 1, idx + 1))

            board[i][j] = temp

            return result

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if searchfrom(i, j, 0):
                        return True
        return False
    
```

# 原始版

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        dirs = [(1, 0),(-1, 0),(0, 1),(0, -1)]
        visited = [[0] * m for _ in range(n)]

        def searchfrom(i, j, word):
            if len(word) == 1:
                return board[i][j] == word
            if board[i][j] != word[0]:
                return False
            visited[i][j] = 1
            result = False
            for di, dj in dirs:
                newi, newj = i + di, j + dj
                if 0 <= newi < n and 0 <= newj < m and visited[newi][newj] == 0:
                    result = result or searchfrom(newi, newj, word[1:])
            visited[i][j] = 0
            return result

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    result = searchfrom(i, j, word)
                    if result == True:
                        return True
        return False
    
```