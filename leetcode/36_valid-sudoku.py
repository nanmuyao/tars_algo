#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 错误示范
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        self.board = board
        self.rows, self.cols = set(), set()
        dot = '.'
        
        for row, values in enumerate(board):
            for col, v in enumerate(values):
                if v == '.':
                    continue
                if not self.is_valid(row, col, v):
                    return False
        return True

    def is_valid(self, row, col, v):
        # 9 * 9
        if self.board[row].count(v) > 1:
            return False
        tmp_col = []
        for row, values in enumerate(self.board):
            if values[col] == '.':
                continue
            tmp_col.append(values[col])
        if tmp_col.count(v) > 1:
            print(4)
            return False

        # 3 * 3
        _col = col // 3
        _row = row // 3
        tmp_col = []
        for i in range(3):
            for j in range(3):
                if self.board[_row * 3 + i][_col * 3 + j] == '.':
                    continue
                else:
                    tmp_col.append(self.board[_row * 3 + i][_col * 3 + j])
        if tmp_col.count(v) > 1:
            return False
        
        return True


# 好简洁
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [{} for i in range(9)]
        cols = [{} for i in range(9)]
        boxs = [{} for i in range(9)]

        for i in range(9):
            for j in range(9):
                v = board[i][j]
                if v == '.':
                    continue

                rows[i][v] = rows[i].get(v, 0) + 1
                cols[j][v] = cols[j].get(v, 0) + 1
                
                box_index = (i//3) * 3 + j // 3
                boxs[box_index][v] = boxs[box_index].get(v, 0) + 1 
                if rows[i][v] > 1 or cols[j][v] > 1 or boxs[box_index][v] > 1:
                    return False
        return True
