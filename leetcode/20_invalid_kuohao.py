class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        map = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        stack = []
        for c in s:
            if c not in map.keys():
                stack.append(c)
            # c -> map[c]
            elif not stack or stack.pop() != map[c]:
                return False
        # return False
        return not stack
