#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        for c in t:
            v = d.get(c, 0) - 1
            if v < 0:
                return False
            d[c] = v
        sum_v = sum(d.values())
        return True if sum_v == 0 else False
