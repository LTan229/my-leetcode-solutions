---
Tags:
  - 设计
  - 字典树
  - 哈希表
  - 字符串
  - H100
Languages:
  - Python
URL: https://leetcode.cn/problems/implement-trie-prefix-tree/submissions/727050706/?envType=study-plan-v2&envId=top-100-liked
---

```python
class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if not char in cur:
                cur[char] = {}
            cur = cur[char]
        cur[None] = True # only mark endpoint
    
    def findend(self, word):
        cur = self.root
        for char in word:
            if char not in cur:
                return None # use none to mark not found
            cur = cur[char]
        return cur

    def search(self, word: str) -> bool:
        end = self.findend(word)
        return (end is not None) and (None in end)

    def startsWith(self, prefix: str) -> bool:
        end = self.findend(prefix)
        return end is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```