# -*- coding: UTF-8 -*-
# leetcode 91
# https://leetcode-cn.com/problems/decode-ways/
# 人与人的思维方式差好多呀，看了个中答案都没看懂
# https://www.youtube.com/watch?v=OjEHST4SXfE
# 102213
class Solution(object):
    result = {}
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def _ways(s):
            if Solution.result.get(s):
                return Solution.result.get(s)
            if s[0:1] == '0':
                return 0
            if len(s) <= 1:
                return 1
            w = _ways(s[1:len(s)])
            prefix = s[0:2]
            if prefix and int(prefix) <= 26:
                w += _ways(s[2:])
            Solution.result[s] = w
            return w
        return _ways(s)
        
print(Solution().numDecodings('302213'))