#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.result = []
        self.cols, self.pies, self.nas = set(), set(), set()
        self.dfs(n, 0, [])
        print(self.result)
        return self.generate_result(n)

    def dfs(self,n, row, cur_state):
        if row >= n:
            self.result.append(cur_state)
            return None
        
        for col in range(n):
            if col in self.cols or (col + row) in self.pies or (col - row) in self.nas:
                continue
            
            self.cols.add(col)
            self.pies.add(col + row)
            self.nas.add(col - row)

            self.dfs(n, row + 1, cur_state + [col])

            self.cols.remove(col)
            self.pies.remove(col + row)
            self.nas.remove(col - row) 
        return None

    def generate_result(self, n):
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in self.result ]
