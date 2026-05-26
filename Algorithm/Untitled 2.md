---
Tags:
  - 字符串
  - DP
  - 回溯
  - H100
Languages:
  - Python
URL: https://leetcode.cn/problems/generate-parentheses/?envType=study-plan-v2&envId=top-100-liked
---
# 回溯 类变量
```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        1:0(1)2
        2:(左)(), ((中)), ()(右) 去重？
        树回溯
        背包：第tot减n位用左/右，后续步骤产生的情况总数
        """
        self.str = ""
        self.results = []

        def backtrace(left, right):
            if right == 0:
                self.results.append(self.str)
                return 
            if left > 0:
                self.str = self.str + '('
                backtrace(left - 1, right)
                self.str = self.str[:-1]
            if right > left:
                self.str = self.str + ')'
                backtrace(left, right - 1)
                self.str = self.str[:-1]
            return
        
        backtrace(n, n)

        return self.results
```
# 回溯，传参
```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        1:0(1)2
        2:(左)(), ((中)), ()(右) 去重？
        树回溯
        背包：第tot减n位用左/右，后续步骤产生的情况总数
        """
        self.results = []

        def backtrace(left, right, string):
            if right == 0:
                self.results.append(string)
                return 
            if left > 0:
                string = string + '('
                backtrace(left - 1, right, string)
                string = string[:-1]
            if right > left:
                string = string + ')'
                backtrace(left, right - 1, string)
                string = string[:-1]
            return
        
        backtrace(n, n, "")

        return self.results
```

# DP
```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        
        # dp[i] i 对括号的所有组合
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""] 
        
        for i in range(1, n + 1):
            # dp[i] = dp[j] + dp[i-1-j]
            for j in range(i):
                for inner in dp[j]:
                    for outer in dp[i - 1 - j]:
                        dp[i].append(f"({inner}){outer}")
        
        return dp[n]

```
