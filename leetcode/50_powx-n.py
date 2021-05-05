#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 1:
            return x
        if n == 0:
            return 1

        # 注意 -n
        if n < 0:
            return 1 / self.myPow(x, -n)

        if n % 2 == 0:
            # 这里很骚气
            return self.myPow(x * x, n/2)
        else:
            return x * self.myPow(x, n - 1)

