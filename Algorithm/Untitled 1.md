---
Tags:
  - 数组
  - 哈希表
  - 前缀和
  - H100
Languages:
  - Python
URL: https://leetcode.cn/problems/subarray-sum-equals-k/description/?envType=study-plan-v2&envId=top-100-liked
---
```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        len_nums = len(nums)
        if len_nums == 0:
            return 0
        d = {0:1}
        count = 0
        cursum = 0
        for i in range(len_nums):
            if i > 0:
                cursum += nums[i - 1]

            presum = cursum - k # k = cursum - presum
            if presum in d:
                count += d[presum]
            
            if not cursum in d:
                d[cursum] = 0
            d[cursum] += 1
        return count
```