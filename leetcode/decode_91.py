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

# 动态规划
class Solution2(object):
    result = {}
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0:1] == '0' or len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        w1, w2 = 1, 1
        for i in range(1, len(s)):
            w = 0
            if s[i] == '0' and s[i-1] == '0':
                return 0
            if s[i] != '0':
                w = w1
            if 10 <= int(s[i-1:i+1]) <= 26:
                w += w2
            w2 = w1
            w1 = w
        return w1
    
print(Solution2().numDecodings('102213'))