# https://leetcode-cn.com/problems/remove-duplicate-letters/submissions/
# 和402类似思路上有重叠，和小操作

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        import collections

        stack = []
        remain_counter = collections.Counter(s)

        for c in s:
            if c not in stack:
                while stack and stack[-1] > c and remain_counter[stack[-1]] >= 1:
                    stack.pop()
                stack.append(c)
            remain_counter[c]-=1

        return ''.join(stack)
