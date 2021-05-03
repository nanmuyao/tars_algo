

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        res = []
        for i, v in enumerate(nums):
            key = target - v
            if key in d:
                res.append(d.get(key))
                res.append(i)
            else:
                d[v] = i
        return res
