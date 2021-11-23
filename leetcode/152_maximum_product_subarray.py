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

    
    
def max_product_subarray(nums):
    if not nums:
        return
    n = len(nums)
    max_list = [nums[0]] * n
    min_list = [nums[0]] * n

    for index in range(1, n):
        value = nums[index]
        max_list[index] = max(max_list[index-1] * value, min_list[index-1] * value, max_list[index-1])
        min_list[index] = min(min_list[index-1] * value, max_list[index-1] * value, min_list[index-1])

    print(max_list)
    print(min_list)
    return max(max_list[n-1], min_list[n-1])
