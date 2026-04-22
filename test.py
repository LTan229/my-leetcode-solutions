class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lennums = len(nums)
        if lennums < 1:
            return lennums
        numset = set(nums)
        maxcnt = 0
        for n in nums:
            if n - 1 in numset:
                continue
            cnt = 1
            while n + 1 in numset:
                cnt += 1
                n += 1
            maxcnt = max(maxcnt, cnt)
        return maxcnt
