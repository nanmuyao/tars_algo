#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        
        l, r = 1, x
        res = 0

        while (l <= r):
            m = (l + r) / 2
            if (m == x/m):
                return m
            elif (m > x/m):
                r = m - 1
            else:
                l = m + 1
                res = m
        # error need return res
        return res


        # if (x == 0 or x == 1):
        #     return x
        # l, r = 1, x
        # res = 0
        # while (l <= r):
        #     m = (l + r) / 2
        #     if m == x/m:
        #         return m
        #     elif m > x / m:
        #         r = m - 1
        #     else:
        #         l = m + 1
        #         res = m
        # return res
