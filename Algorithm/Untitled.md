---
Tags:
  - 哈希表
  - 字符串
  - 滑动窗口
Languages:
  - Python
URL:
---
```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lenp = len(p)
        lens = len(s)
        if lenp > lens:
            return []
        d_p = {}
        d_s = {}
        for i in range(lenp):
            if not p[i] in d_p:
                d_p[p[i]] = 0
            d_p[p[i]] += 1
            if not s[i] in d_s:
                d_s[s[i]] = 0
            d_s[s[i]] += 1
        i = 0
        j = lenp - 1 # [i, j]
        result = []
        while True:
            if d_p == d_s:
                result.append(i)
            d_s[s[i]] -= 1
            if d_s[s[i]] == 0:
                d_s.pop(s[i])
            i += 1
            j += 1
            if j == lens:
                break
            if not s[j] in d_s:
                d_s[s[j]] = 0
            d_s[s[j]] += 1
        return result
```