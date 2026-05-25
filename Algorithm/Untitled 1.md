---
Tags:
Languages:
  - Python
URL: https://leetcode.cn/problems/course-schedule/?envType=study-plan-v2&envId=top-100-liked
---

```python
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegs = [0 for _ in range(numCourses)] # in
        reliant = {} # r[b] = [a,...]

        for a, b in prerequisites: # b->a
            indegs[a] += 1
            if not b in reliant:
                reliant[b] = []
            reliant[b].append(a)
        
        q = deque([])

        for idx, ind in enumerate(indegs):
            if ind == 0:
                q.append(idx)

        learnt = 0
        
        while q:
            cur = q.popleft()
            learnt += 1
            if not cur in reliant:
                continue
            for c in reliant[cur]:
                indegs[c] -= 1
                if indegs[c] == 0:
                    q.append(c)
        
        if learnt < numCourses:
            return False
        
        return True
            
```