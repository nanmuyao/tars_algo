# https://leetcode-cn.com/problems/minimum-size-subarray-sum/submissions/

# 滑动窗口

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size = 0

        for index_1 in range(len(nums)):
            res = 0
            for index_2 in range(index_1, len(nums)):
                res+=nums[index_2]
                if res >= target:
                    size = (index_2 - index_1 + 1) if size == 0 else min((index_2 - index_1) + 1, size)
                    break

        return size
