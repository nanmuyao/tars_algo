# https://leetcode-cn.com/problems/maximum-product-subarray/submissions/

# 超时了
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        global_max = nums[0]
        for index, value in enumerate(nums):
            global_max = max(global_max, nums[index])
            round_max = nums[index]
            for cur_value in range(index + 1, len(nums)):
                round_max *= nums[cur_value]
                global_max = max(global_max, round_max)

        return global_max
