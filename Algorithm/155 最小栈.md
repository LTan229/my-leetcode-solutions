---
Tags:
  - 栈
  - 设计
  - H100
Languages:
  - Python
URL: https://leetcode.cn/problems/min-stack/?envType=study-plan-v2&envId=top-100-liked
---

```python
class MinStack:

    def __init__(self):
        self.list = [] # val, min up til now

    def push(self, val: int) -> None:
        if not self.list:
            mini = val
        else:
            mini = min(self.list[-1][1], val)
        self.list.append((val, mini))

    def pop(self) -> None:
        self.list.pop()        

    def top(self) -> int:
        return self.list[-1][0]        

    def getMin(self) -> int:
        return self.list[-1][1]  
```

# Dummy head
- `pop`、`top` 和 `getMin` 操作总是在 **非空栈** 上调用
```python
class MinStack:

    def __init__(self):
        self.stack = [(0,inf)]
        
    def push(self, val: int) -> None:
        self.stack.append((val, min(val, self.stack[-1][1])))
        
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]
```